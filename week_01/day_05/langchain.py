from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

messages = [
    SystemMessage(
        content="You are a helpful AI assistant."
    )
]

print("Type 'exit' to end the chat.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    messages.append(
        HumanMessage(
            content=user_input
        )
    )

    response = llm.invoke(messages)

    print(f"\nAssistant: {response.content}\n")

    messages.append(
        AIMessage(
            content=response.content
        )
    )