from loaders import load_all_documents
from splitter import split_documents
from vector_store import store_documents


DATA_FOLDER = "data"


def ingest_documents():

    print("Loading documents...")

    documents = load_all_documents(DATA_FOLDER)

    print(f"Loaded {len(documents)} documents.")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Generated {len(chunks)} chunks.")

    print("Generating embeddings and storing in PGVector...")

    store_documents(chunks)

    print("Documents indexed successfully.")