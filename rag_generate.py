import os
import requests
import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Initialize embedding function & Chroma client
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

client = chromadb.Client(Settings(persist_directory="./chroma_db"))

collection = client.get_collection("terraform_docs")

def retrieve_docs(query, top_k=5):
    # Embed the query
    query_embedding = embedding_function([query])[0]

    # Query Chroma for relevant docs
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    
    # results["documents"] is a list of list of docs, take first list
    return results["documents"][0]

def generate_prompt(context_chunks, user_query):
    context_text = "\n---\n".join(context_chunks)
    prompt = f"""
You are a Terraform expert. Given the following documentation context:

{context_text}

Use this context to write a Terraform configuration for the user request:

{user_query}

Terraform config:
"""
    return prompt

def call_llm(prompt):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

    url = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={api_key}"

    headers = {"Content-Type": "application/json"}

    json_data = {
        "prompt": {
            "text": prompt
        },
        "temperature": 0,
        "maxOutputTokens": 300
    }

    response = requests.post(url, headers=headers, json=json_data)
    response.raise_for_status()

    result = response.json()
    return result["candidates"][0]["output"]

if __name__ == "__main__":
    query = input("Enter your Terraform request: ")

    docs = retrieve_docs(query)
    print("\nRetrieved relevant docs:")
    for d in docs:
        print("-", d)

    prompt = generate_prompt(docs, query)
    print("\nGenerated prompt for LLM:")
    print(prompt)

    terraform_code = call_llm(prompt)
    print("\nGenerated Terraform configuration:")
    print(terraform_code)
