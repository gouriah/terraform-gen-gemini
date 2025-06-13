from chroma_client import get_collection

# Get shared collection instance
collection = get_collection()

# Get user query input
query = input("🔍 Enter a query to search Terraform docs: ")

# Search vector DB for top relevant docs (increase n_results to 10)
results = collection.query(query_texts=[query], n_results=10)

# Display results
if results["documents"][0]:
    print("\n📄 Top Relevant Documents:")
    for doc in results["documents"][0]:
        print("\n---\n", doc)
else:
    print("⚠️ No documents found for your query.")
