from langchain_community.callbacks.manager import get_openai_callback


def execute_chain(chain, question: str):

    with get_openai_callback() as cb:

        answer = chain.invoke(
            {
                "question": question
            }
        )

        return {
            "answer": answer,
            "prompt_tokens": cb.prompt_tokens,
            "completion_tokens": cb.completion_tokens,
            "total_tokens": cb.total_tokens,
            "estimated_cost": cb.total_cost,
        }