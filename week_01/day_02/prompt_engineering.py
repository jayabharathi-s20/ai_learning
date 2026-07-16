from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

topic = input("Enter a python topic: ")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": """
You are a senior Python instructor who teaches beginners.

Rules:
1. Answer ONLY Python-related questions.
2. If the user asks about any language other than Python (Java, C, C++, JavaScript, Go, etc.) or any non-programming topic, politely reply:
   "Sorry, I can only answer Python-related questions."
3. Do not compare Python with other languages unless the question is specifically about Python.
4. Explain Python concepts in simple, friendly, and beginner-friendly language.
5. Always include practical examples when appropriate.
"""
        },
        {
            "role": "user",
            "content": f"""
Task:
Explain {topic}.

Audience:
Beginner programmers.

Requirements:
- Maximum 150 words.
- Use simple English.
- Give one real-world example.
- Mention three key points.

Output Format:

# Definition

# Key Points

# Real-world Example

# Summary
"""
        }
    ]
)

print(response.choices[0].message.content)