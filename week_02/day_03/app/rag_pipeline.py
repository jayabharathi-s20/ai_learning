from pathlib import Path

from .loader import load_pdf
from .create_embeddings import vector_store

PDF_PATH = Path(__file__).parent / "data" / "ai_learning.pdf"

chunks = load_pdf(str(PDF_PATH))

vector_store.add_documents(chunks)

print(f"{len(chunks)} chunks indexed successfully.")