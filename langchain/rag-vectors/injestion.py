import os

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter

INDEX_NAME = "blogs-embeddings-index"
BLOGS_FILE = "blog.txt"

if __name__ == "__main__":
    print(f"hello pinecone")
    loader = TextLoader(BLOGS_FILE)
    doc = loader.load()

    print("splitting ...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks = text_splitter.split_documents(doc)
    print(f"created {len(chunks)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    print("injestion")
    vector_store = PineconeVectorStore.from_documents(
        chunks,
        embeddings,
        pinecone_api_key=os.environ["PINECONE_API_KEY"],
        index_name=INDEX_NAME,
    )
