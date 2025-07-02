import os

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone
from langchain_text_splitters import CharacterTextSplitter

INDEX_NAME = "blogs-embeddings-index"

if __name__ == "__main__":
    print(f"hello pinecone")
