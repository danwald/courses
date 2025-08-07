from pathlib import Path

from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter

PERSIST_DIRECTORY = "./.chroma"
COLLECTION_NAME = "rag-chroma"

URLS = (
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
)

if __name__ == "__main__":
    docs = [WebBaseLoader(url).load() for url in URLS]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )

    doc_splits = text_splitter.split_documents(docs_list)

    if not Path(PERSIST_DIRECTORY).exists():
        print(f"Ingesting {len(docs_list)} docs w/{len(doc_splits)} tokens")
        vectorstore = Chroma.from_documents(
            documents=doc_splits,
            collection_name=COLLECTION_NAME,
            embedding=OpenAIEmbeddings(),
            persist_directory=PERSIST_DIRECTORY,
        )
    else:
        print(f"Reloading docs from {PERSIST_DIRECTORY}")

    retriever = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=OpenAIEmbeddings(),
    ).as_retriever()
