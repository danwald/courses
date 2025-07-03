import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from settings import INDEX_NAME

from langchain import hub  # type: ignore[attr-defined]
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

if __name__ == "__main__":
    print("retrieval")

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    query = "what is pinecone in machine learning?"
    chain = PromptTemplate.from_template(template=query) | llm
    result = chain.invoke(input={})

    vector_store = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

    ret_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(llm, ret_qa_chat_prompt)
    retrival_chain = create_retrieval_chain(
        retriever=vector_store.as_retriever(), combine_docs_chain=combine_docs_chain
    )

    result = retrival_chain.invoke(input={"input": query})

    print(result)
