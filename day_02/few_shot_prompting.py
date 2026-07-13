from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

english = input("Enter an English sentence: ")

prompt = f"""
Translate English to french.

English: Hello
French: Bonjour

English: Thank you
French: Merci

English: Good Night
French: Bonne nuit

English: See you later
French: À plus tard

English: {english}
French:
"""

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nFrench Translation:")
print(response.choices[0].message.content)