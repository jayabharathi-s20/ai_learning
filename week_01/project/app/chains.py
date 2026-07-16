from langchain_core.output_parsers import StrOutputParser

from app.llm import llm
from app.prompts import query_prompt

output_parser = StrOutputParser()

query_chain = query_prompt | llm | output_parser