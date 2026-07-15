from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

from config import OPENAI_API_KEY, DATABASE_URL

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_documents",
    connection=DATABASE_URL,
    use_jsonb=True
)