import chromadb
from chromadb.config import Settings
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding_function = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

client = chromadb.Client(Settings(persist_directory="./chroma_db"))

def get_collection():
    return client.get_or_create_collection(
        name="terraform_docs",
        embedding_function=embedding_function
    )
