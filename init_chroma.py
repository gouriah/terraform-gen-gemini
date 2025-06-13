from chroma_client import get_collection
import os

# Get shared collection instance
collection = get_collection()

# Path to documentation files
docs_dir = "./data"

# Add each file's content as a document in the vector database
for filename in os.listdir(docs_dir):
    file_path = os.path.join(docs_dir, filename)
    if not filename.endswith((".md", ".txt")):
        continue

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"Adding {filename} to Chroma DB...")
            collection.add(
                documents=[content],
                ids=[filename]
            )
    except Exception as e:
        print(f"⚠️ Skipped file {filename}: {e}")

print("✅ Terraform docs successfully added to Chroma DB.")
print(collection.get())
