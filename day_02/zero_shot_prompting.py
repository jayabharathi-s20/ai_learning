from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

english = input("Enter an English sentence: ")

prompt = f"""
Translate the following English sentence into french.

Sentence:
{english}
"""

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nFrench Translation:")
print(response.choices[0].message.content)