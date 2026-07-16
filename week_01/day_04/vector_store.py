from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from config import OPENAI_API_KEY, DATABASE_URL,EMBEDDINGS_MODEL

embeddings = OpenAIEmbeddings(
    model=EMBEDDINGS_MODEL,
    api_key=OPENAI_API_KEY
)

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_documents",
    connection=DATABASE_URL,
    use_jsonb=True
)