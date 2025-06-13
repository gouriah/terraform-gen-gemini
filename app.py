import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load docs from /data folder
def load_docs(directory="./data"):
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith(".md") or filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

# Find docs containing relevant keywords
def find_relevant_docs(query, docs):
    relevant = []
    for doc in docs:
        if query.lower() in doc.lower():
            relevant.append(doc)
    return relevant

# Generate Terraform config via Gemini Flash model
def generate_config(prompt, context):
    full_prompt = f"""
You are an expert Terraform practitioner.

Given the following Terraform documentation and this user request, generate a clean, working Terraform configuration in HCL (HashiCorp Configuration Language). No extra explanation.

DOCUMENTATION:
{context}

USER REQUEST:
{prompt}

Only output the final Terraform configuration code.
"""
    # Swapped to high-quota Flash model
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    response = model.generate_content(full_prompt)
    return response.text

# Streamlit UI
st.title("🚀 Terraform Config Generator (Gemini Flash)")

user_input = st.text_area("Enter your infrastructure request:")

if st.button("Generate Config"):
    if user_input:
        docs = load_docs()
        relevant_docs = find_relevant_docs("ec2", docs)
        context = "\n\n".join(relevant_docs) if relevant_docs else ""

        config = generate_config(user_input, context)
        st.subheader("✅ Generated Terraform Configuration:")
        st.code(config, language='hcl')

        # Save to file
        output_path = "./output/generated_config_web.tf"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(config)

        st.success(f"✅ Config saved to {output_path}")
    else:
        st.warning("Please enter a request before generating.")
