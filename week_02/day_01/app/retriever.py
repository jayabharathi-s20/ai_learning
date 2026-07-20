from vector_store import semantic_search


def retrieve_documents(query: str, k: int = 3):

    results = semantic_search(
        query=query,
        k=k,
    )

    return results