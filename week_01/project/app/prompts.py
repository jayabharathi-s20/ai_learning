from langchain_core.prompts import ChatPromptTemplate

query_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Answer the user's question clearly and accurately."
        ),
        (
            "human",
            "{question}"
        )
    ]
)