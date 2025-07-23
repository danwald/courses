from langchain_community.chat_models.openai import ChatOpenAI
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from langchain import hub  # type: ignore
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


def run_llm(query: str) -> dict[str, str]:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = PineconeVectorStore(
        embedding=embeddings, index_name="langchain-docs-index"
    )
    chat = ChatOpenAI(verbose=True, temperature=0)
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_docs_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)

    qa = create_retrieval_chain(
        retriever=vectorstore.as_retriever(), combine_docs_chain=stuff_docs_chain
    )
    result = qa.invoke(input={"input": query})
    return {
        "result": result["answer"],
        "query": query,
        "source_documents": result["context"],
    }


if __name__ == "__main__":
    result = run_llm("What is a langchain chain")
    print(result["result"])
