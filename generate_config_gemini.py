import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load all documentation files into memory
def load_docs(directory="./data"):
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith(".md") or filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

# Simple context retriever: search docs for keyword match
def find_relevant_docs(query, docs):
    relevant = []
    for doc in docs:
        if query.lower() in doc.lower():
            relevant.append(doc)
    return relevant

# Generate Terraform config via Gemini Pro
def generate_config(prompt, context):
    full_prompt = f"""
You are an expert Terraform practitioner.

Given the following AWS Terraform documentation and user request, generate a clean, working Terraform configuration in HCL (HashiCorp Configuration Language). No extra explanation.

DOCUMENTATION:
{context}

USER REQUEST:
{prompt}

Only output the final Terraform configuration code.
"""
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    response = model.generate_content(full_prompt)
    return response.text

if __name__ == "__main__":
    query = input("🔍 Enter your infrastructure request: ")
    docs = load_docs()
    relevant_docs = find_relevant_docs("ec2", docs)  # or use query keyword

    if not relevant_docs:
        print("⚠️ No matching docs found for your query.")
        context = ""
    else:
        context = "\n\n".join(relevant_docs)

    terraform_config = generate_config(query, context)

    print("\n✅ Generated Terraform Configuration:\n")
    print(terraform_config)

    with open("./output/generated_config.tf", "w", encoding="utf-8") as f:
        f.write(terraform_config)

    print("\n✅ Config saved to ./output/generated_config.tf")
