from contextlib import asynccontextmanager

from fastapi import FastAPI

from ingest import ingest_documents
from retriever import retrieve_documents


@asynccontextmanager
async def lifespan(app: FastAPI):


    print("\nStarting RAG Application...")

    ingest_documents()

    print("Application started successfully.\n")

    yield

    print("Application shutting down...")


app = FastAPI(
    title="RAG Application",
    version="1.0.0",
    lifespan=lifespan,
)


@app.post("/ingest")
def ingest():


    ingest_documents()

    return {
        "status": "success",
        "message": "Documents indexed successfully."
    }


@app.get("/search")
def search(query: str):


    documents = retrieve_documents(query)

    response = []

    for document in documents:

        response.append(
            {
                "content": document.page_content,
                "metadata": document.metadata
            }
        )

    return {
        "query": query,
        "results": response
    }