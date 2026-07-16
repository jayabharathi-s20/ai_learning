from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role":"system",
        "content":"You are a helpful AI assistant"
    }
]

print("Type 'exit to end the chat.\n")

while True:

    user_input=input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    messages.append(
        {
            "role":"user","content":user_input
        }
    )

    #API CALL
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    assistant_reply=response.choices[0].message.content
    print(f"\nAssistant: {assistant_reply}\n")

    messages.append(
        {
            "role":"assistant",
            "content":assistant_reply
        }
    )


