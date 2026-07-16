from fastapi import APIRouter

from app.schemas import QueryRequest, QueryResponse
from app.chains import query_chain
from app.cost_tracker import execute_chain

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query_llm(request: QueryRequest):

    result = execute_chain(
        query_chain,
        request.question
    )

    return QueryResponse(
        answer=result["answer"],
        prompt_tokens=result["prompt_tokens"],
        completion_tokens=result["completion_tokens"],
        total_tokens=result["total_tokens"],
        estimated_cost=result["estimated_cost"]
    )