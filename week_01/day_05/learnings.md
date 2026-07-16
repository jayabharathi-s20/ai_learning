# Day 05 – LangChain

## Objective

Learn how LangChain simplifies building applications using Large Language Models (LLMs) by providing reusable components for prompts, chat models, memory, and chains.

---

# 1. What is LangChain?

LangChain is an open-source framework that simplifies developing applications powered by Large Language Models (LLMs).

Instead of manually handling API requests and responses, LangChain provides high-level abstractions for common tasks such as:

- Prompt management
- Chat models
- Memory
- Chains
- Document loading
- Retrieval
- Agents

It allows developers to focus on application logic rather than low-level API handling.

---

# 2. Why Use LangChain?

Without LangChain, developers need to:

- Manage API requests manually
- Format prompts
- Store conversation history
- Parse responses
- Handle multiple LLM interactions

LangChain simplifies these tasks by providing reusable components.

---

# 3. Chat Models

A chat model is an interface that allows communication with Large Language Models.

Example:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)
```

### Explanation

**model**

Specifies which OpenAI model to use.

Example:

```python
model="gpt-4o-mini"
```

---

**temperature**

Controls response randomness.

```text
0.0 → Deterministic
1.0 → Creative
```

---

# 4. Message Types

LangChain structures conversations using message objects.

---

## SystemMessage

Provides instructions to the model.

Example:

```python
SystemMessage(
    content="You are a helpful AI assistant."
)
```

---

## HumanMessage

Represents the user's input.

Example:

```python
HumanMessage(
    content="What is AI?"
)
```

---

## AIMessage

Represents the assistant's response.

Example:

```python
AIMessage(
    content="Artificial Intelligence is..."
)
```

---

# 5. Conversation History

Instead of sending only the latest question, previous messages are stored.

Example:

```python
messages = [
    SystemMessage(...),
    HumanMessage(...),
    AIMessage(...)
]
```

Each new message is appended to this list before invoking the model.

This enables the model to remember previous interactions and generate context-aware responses.

---

# 6. Invoking the Model

The complete conversation history is passed to the model.

Example:

```python
response = llm.invoke(messages)
```

The model considers the entire conversation when generating the next response.

---

# 7. Why Store Previous Messages?

If only the latest question is sent:

```text
User:
My name is John.

User:
What is my name?
```

The model has no previous context and cannot answer correctly.

If previous messages are stored:

```text
System Message
↓

Human Message
↓

AI Message
↓

Human Message
↓

AI Message
```

The model remembers earlier interactions and provides context-aware responses.

---

# 8. What are Chains?

A Chain connects multiple LangChain components into a workflow.

Example:

```text
Prompt
   │
   ▼
LLM
   │
   ▼
Output Parser
```

Instead of manually calling each component, the chain executes them in sequence.

Example:

```python
chain = prompt | llm | output_parser
```

Running the chain:

```python
response = chain.invoke(
    {
        "question": "What is AI?"
    }
)
```

---

# 9. Why Use Chains?

Without Chains:

```text
Create Prompt
↓

Call LLM
↓

Extract Response
↓

Return Result
```

Each step is written manually.

With Chains:

```text
Prompt
↓

LLM
↓

Output Parser
↓

Final Output
```

The workflow is reusable, cleaner, and easier to maintain.

---

# 10. LangChain Workflow

```text
User Input
      │
      ▼
HumanMessage
      │
      ▼
Conversation History
      │
      ▼
ChatOpenAI
      │
      ▼
AI Response
      │
      ▼
Store Response
      │
      ▼
Continue Conversation
```

---

# Key Learnings

- Learned what LangChain is and why it is used.
- Understood how LangChain simplifies LLM application development.
- Created chat models using `ChatOpenAI`.
- Learned the purpose of `SystemMessage`, `HumanMessage`, and `AIMessage`.
- Maintained conversation history for context-aware interactions.
- Invoked LLMs using LangChain instead of direct OpenAI API calls.
- Learned how Chains combine prompts, models, and output parsers into reusable workflows.
- Understood how LangChain reduces boilerplate code and improves maintainability.

---

# Outcome

By the end of Day 05, I am able to:

- Build conversational AI applications using LangChain.
- Manage conversation history using LangChain message objects.
- Use ChatOpenAI to interact with OpenAI models.
- Understand and implement LangChain Chains.
- Explain how LangChain simplifies LLM workflows compared to direct API integration.