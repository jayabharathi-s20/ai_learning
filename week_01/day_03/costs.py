from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_input = input("Ask me anything: ")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":user_input}
    ]
)
print(response.choices[0].message.content)


prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

print(f"Prompt Tokens      : {prompt_tokens}")
print(f"Completion Tokens  : {completion_tokens}")
print(f"Total Tokens       : {total_tokens}")

input_price_per_million = 0.15
output_price_per_million = 0.60

input_cost = (prompt_tokens/1000000) * input_price_per_million
output_cost = (completion_tokens/1000000) * output_price_per_million
total_cost = input_cost + output_cost

print(f"Input Cost         : ${input_cost:.8f}")
print(f"Output Cost        : ${output_cost:.8f}")
print(f"Total Cost         : ${total_cost:.8f}")