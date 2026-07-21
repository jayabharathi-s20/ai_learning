from langchain_openai import OpenAIEmbeddings

from config import (
    OPENAI_API_KEY,
    EMBEDDINGS_MODEL,
)

embeddings = OpenAIEmbeddings(
    api_key=OPENAI_API_KEY,
    model=EMBEDDINGS_MODEL,
)