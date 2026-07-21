from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from .config import (
    OPENAI_API_KEY,
    EMBEDDINGS_MODEL,
    DATABASE_URL,
    COLLECTION_NAME
)

embeddings = OpenAIEmbeddings(
    model=EMBEDDINGS_MODEL,
    api_key=OPENAI_API_KEY
)

vector_store = PGVector(
    embeddings=embeddings,
    collection_name=COLLECTION_NAME,
    connection=DATABASE_URL,
    use_jsonb=True
)