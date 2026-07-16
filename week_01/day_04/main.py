from load_documents import load_pdf
from vector_store import vector_store

documents = load_pdf("data/ai_learning.pdf")
vector_store.add_documents(documents)

print("Embeddings stored successfully.")

query = input("Enter your question: ")

results = vector_store.similarity_search(query, k=3)

print("\nResults:\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}:")
    print(doc.page_content)
    print("-" * 50)