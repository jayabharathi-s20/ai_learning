from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from langchain_openai import ChatOpenAI

from .config import OPENAI_API_KEY, OPENAI_MODEL
from .loader import load_pdf
from .create_embeddings import vector_store
from .retriever import retriever

app = FastAPI()

llm = ChatOpenAI(
    model=OPENAI_MODEL,
    api_key=OPENAI_API_KEY
)

PDF_PATH = Path(__file__).parent / "data" / "ai_learning.pdf"


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG API is running"}


@app.post("/index")
def index_pdf():
    try:
        chunks = load_pdf(str(PDF_PATH))

        vector_store.add_documents(chunks)

        return {
            "message": "PDF indexed successfully",
            "chunks_indexed": len(chunks)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/ask")
def ask(question: Question):
    try:
        docs = retriever.invoke(question.question)

        if not docs:
            return {"answer": "No relevant information found."}

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = f"""
You are a helpful assistant.

Answer ONLY using the context below.

If the answer is not available in the context, say:
'I couldn't find that information in the provided document.'

Context:
{context}

Question:
{question.question}
"""

        response = llm.invoke(prompt)

        return {
            "question": question.question,
            "answer": response.content
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )