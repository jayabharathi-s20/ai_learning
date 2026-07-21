from langchain_postgres import PGVector

from config import (
    DATABASE_URL,
    COLLECTION_NAME,
)

from embeddings import embeddings


vector_store = PGVector(
    embeddings=embeddings,
    connection=DATABASE_URL,
    collection_name=COLLECTION_NAME,
    use_jsonb=True,
)


def store_documents(chunks):

    vector_store.add_documents(chunks)

    print(f"{len(chunks)} chunks stored successfully.")


def semantic_search(query, k=3):

    results = vector_store.similarity_search(
        query=query,
        k=k,
    )

    return results