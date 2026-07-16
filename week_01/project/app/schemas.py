from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    estimated_cost: float