from typing import Any

from langchain_community.chat_models.openai import ChatOpenAI
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from langchain import hub  # type: ignore
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain


def run_llm(
    query: str, chat_history: list[dict[str, Any]] | None = None
) -> dict[str, Any]:
    chat_history = chat_history or []
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = PineconeVectorStore(
        embedding=embeddings, index_name="langchain-docs-index"
    )
    chat = ChatOpenAI(verbose=True, temperature=0)

    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_docs_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)

    history_aware_retriever = create_history_aware_retriever(
        llm=chat, retriever=vectorstore.as_retriever(), prompt=rephrase_prompt
    )
    qa = create_retrieval_chain(
        retriever=history_aware_retriever, combine_docs_chain=stuff_docs_chain
    )
    result = qa.invoke(input={"input": query, "chat_history": chat_history})
    return {
        "result": result["answer"],
        "query": query,
        "source_documents": result["context"],
    }


if __name__ == "__main__":
    result = run_llm("What is a langchain chain")
    print(result["result"])
