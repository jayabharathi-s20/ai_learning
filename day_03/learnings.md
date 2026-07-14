# Day 03 – OpenAI API

## Objective

Learn how to use Large Language Models (LLMs) programmatically by integrating the OpenAI API into Python applications.

---

# 1. Calling the OpenAI API

## What is an API?

API stands for **Application Programming Interface**.

An API acts as a bridge between two applications. Instead of building and running an LLM on your own machine, your application sends a request to OpenAI's servers through the API. OpenAI processes the request using the selected model and returns the generated response.


---

## OpenAI API Workflow

```text
Python Application
        │
        ▼
Create API Request
        │
        ▼
Authenticate using API Key
        │
        ▼
Send Request to OpenAI
        │
        ▼
OpenAI Model Processes Prompt
        │
        ▼
Generate Response
        │
        ▼
Return Response Object
        │
        ▼
Extract AI Response
```

---

## Step 1: Install Required Packages

```bash
pip install openai python-dotenv
```

---

## Step 2: Store the API Key

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key
```

> **Note:** Never hardcode API keys inside source code.

---

## Step 3: Load the API Key

```python
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

### Explanation

#### `load_dotenv()`

Loads environment variables from the `.env` file.

#### `os.getenv("OPENAI_API_KEY")`

Reads the API key from the environment.

#### `OpenAI()`

Creates a client object that communicates with OpenAI servers.

---

## Step 4: Create the API Request

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Explain Python decorators."
        }
    ]
)
```

### Explanation

#### `client`

Represents the OpenAI client.

#### `chat`

Uses the Chat Completions API.

#### `completions`

Requests the model to generate a completion.

#### `create()`

Sends the request to OpenAI.

---

### `model`

Specifies which model to use.

Example:

```python
model="gpt-4o-mini"
```

Different models differ in:

- Intelligence
- Speed
- Cost
- Context Window

---

### `messages`

Contains the conversation.

```python
messages=[
    {
        "role":"user",
        "content":"Explain Python decorators."
    }
]
```

Each message contains:

#### `role`

Defines who is speaking.

Possible values:

- `system`
- `user`
- `assistant`

Example:

```python
{
    "role":"system",
    "content":"You are a Python expert."
}
```

```python
{
    "role":"user",
    "content":"Explain Python."
}
```

```python
{
    "role":"assistant",
    "content":"Python is..."
}
```

#### `content`

Contains the actual text sent to the model.

---

## Step 5: Receive the Response

The API returns a response object.

```text
Request
   │
   ▼
OpenAI
   │
   ▼
Response Object
```

Print the complete response.

```python
print(response)
```

The response contains:

- Response ID
- Model Name
- Generated Content
- Token Usage
- Finish Reason
- Metadata

---

## Step 6: Extract the AI Response

```python
print(response.choices[0].message.content)
```

### Explanation

- `choices` → List of generated responses.
- `[0]` → Accesses the first response.
- `message` → Assistant message.
- `content` → Generated text.

---

# 2. Tuning Parameters

## What is Parameter Tuning?

Parameter tuning means controlling how the model behaves.

Instead of changing the prompt, you adjust settings that influence:

- Creativity
- Response Length
- Randomness
- Repetition
- Topic Diversity

---

## 2.1 `model`

Selects which model to use.

```python
model="gpt-4o-mini"
```

### Example

#### gpt-4o-mini

- Faster
- Lower Cost
- Good for learning and testing

#### gpt-4o

- Better reasoning
- Higher quality
- Higher cost

---

## 2.2 `temperature`

Controls creativity.

Range:

```text
0 → 2
```

### Low Temperature

```python
temperature=0.2
```

Prompt:

```text
Suggest a coffee shop name.
```

Output:

```text
Daily Brew
```

Running the same prompt multiple times usually produces similar results.

---

### High Temperature

```python
temperature=1.2
```

Possible Outputs:

```text
Moonlight Coffee
```

```text
Roasted Dreams
```

```text
Bean Horizon
```

Each execution may generate a different answer.

### Best Use Cases

Low Temperature:

- Coding
- Debugging
- Technical Questions

High Temperature:

- Story Writing
- Brainstorming
- Creative Content

---

## 2.3 `max_completion_tokens`

Limits the maximum response length.

```python
max_completion_tokens=50
```

Prompt:

```text
Explain Python.
```

Output:

```text
Python is a programming language used for web development, AI and automation.
```

Increase it to:

```python
max_completion_tokens=200
```

The response becomes much more detailed.

### Benefits

- Reduces API cost
- Prevents unnecessarily long responses

---

## 2.4 `top_p`

Controls diversity of word selection.

```python
top_p=1
```

The model considers almost all probable next words.

```python
top_p=0.3
```

The model considers only the most probable words.

> **Note:** Usually adjust **either `temperature` or `top_p`**, not both aggressively.

---

## 2.5 `frequency_penalty`

Reduces repeated words.

Without Penalty:

```text
Python is easy.

Python is powerful.

Python is popular.
```

With:

```python
frequency_penalty=1
```

Output:

```text
Python is easy.

It is powerful.

The language is widely used.
```

---

## 2.6 `presence_penalty`

Encourages introducing new ideas.

Prompt:

```text
Give me programming tips.
```

Without Penalty:

```text
Practice coding.

Practice coding daily.

Practice coding regularly.
```

With:

```python
presence_penalty=1
```

Output:

```text
Practice coding.

Read documentation.

Contribute to open source.

Build projects.

Teach others.
```

---

## Combined Example

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"Suggest a startup idea."
        }
    ],
    temperature=0.8,
    max_completion_tokens=120,
    top_p=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.5
)
```

---

# 3. Calculating Usage Cost

## Why Calculate Usage Cost?

Every API request costs money.

The total cost depends on:

- Input Tokens
- Output Tokens
- Model Pricing

Monitoring token usage helps estimate expenses and optimize prompts.

---

## Step 1: Read Token Usage

```python
prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens
```

Example:

```text
Prompt Tokens      : 10
Completion Tokens  : 328
Total Tokens       : 338
```

---

## Step 2: Understand Pricing

Example (gpt-4o-mini):

```text
Input  : $0.15 per 1 million tokens
Output : $0.60 per 1 million tokens
```

Meaning:

```text
1,000,000 input tokens
        ↓
      $0.15
```

If only 10 tokens are used, you pay only for those 10 tokens.

---

## Step 3: Cost Formula

```text
Input Cost =
(Prompt Tokens ÷ 1,000,000) × Input Price
```

```text
Output Cost =
(Completion Tokens ÷ 1,000,000) × Output Price
```

```text
Total Cost =
Input Cost + Output Cost
```

---

## Step 4: Python Implementation

```python
INPUT_PRICE_PER_MILLION = 0.15
OUTPUT_PRICE_PER_MILLION = 0.60

input_cost = (
    prompt_tokens / 1_000_000
) * INPUT_PRICE_PER_MILLION

output_cost = (
    completion_tokens / 1_000_000
) * OUTPUT_PRICE_PER_MILLION

total_cost = input_cost + output_cost
```

---

## Example Calculation

Suppose:

```text
Prompt Tokens      : 10
Completion Tokens  : 328
```

### Input Cost

```text
(10 / 1,000,000) × 0.15
= 0.00000150
```

### Output Cost

```text
(328 / 1,000,000) × 0.60
= 0.00019680
```

### Total Cost

```text
0.00000150 + 0.00019680
= 0.00019830
```

---

## Why is Usage Cost Important?

Calculating usage cost helps you:

- Estimate API expenses.
- Compare model costs.
- Optimize prompt size.
- Reduce unnecessary token usage.
- Build scalable AI applications within budget.

---

# Key Learnings

- Learned how to integrate OpenAI models into Python applications.
- Understood the complete API request-response lifecycle.
- Learned how to authenticate using an API key.
- Explored the purpose of the Chat Completions API.
- Learned how to tune model behavior using parameters such as `temperature`, `max_completion_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty`.
- Understood token usage and how it impacts API pricing.
- Implemented usage cost calculation using token counts and model pricing.
- Built hands-on Python examples for API integration, parameter tuning, and cost estimation.

---

# Outcome

By the end of Day 03, I am able to:

- Programmatically interact with OpenAI LLMs.
- Call the OpenAI API from Python.
- Tune model parameters based on different use cases.
- Monitor token usage and estimate API costs.
- Integrate LLM capabilities into Python applications.