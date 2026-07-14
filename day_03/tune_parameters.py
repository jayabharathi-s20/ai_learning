from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Suggest a unique name for a coffee shop and explain why it is a good name."
        }
    ],
    temperature=0.8,
    # temperature=1.0,
    max_completion_tokens=50,
    # max_completion_tokens=30,
    top_p=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.5
)

print(response.choices[0].message.content)
# print(response)