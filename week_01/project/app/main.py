from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="LLM Query API",
    description="FastAPI application for querying OpenAI models using LangChain.",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to the LLM Query API!"
    }