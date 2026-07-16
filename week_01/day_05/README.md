# Day 05 - LangChain

## Overview

This folder contains my Day 05 AI learning exercises on **LangChain**.

The objective of this task is to understand how LangChain simplifies working with Large Language Models (LLMs). Instead of directly calling the OpenAI API, LangChain provides reusable components for managing prompts, conversations, and chaining together different operations.

In this exercise, I built a simple conversational AI application using LangChain's `ChatOpenAI` class. The application maintains conversation history, allowing the model to remember previous interactions and provide context-aware responses.

---

## Project Structure

```text
day_05/
│
├── README.md
├── learnings.md
└── langchain.py
```


---

### `langchain.py`

Implements a simple chatbot using LangChain.

The program:

- Loads environment variables.
- Creates a ChatOpenAI model.
- Initializes the conversation with a System Message.
- Accepts user input continuously.
- Maintains conversation history.
- Sends the conversation to the LLM.
- Prints the assistant's response.
- Stores previous messages for contextual conversations.

Run the application:

```bash
python langchain.py
```

---

## Installation

Install the required packages:

```bash
pip install langchain
pip install langchain-openai
pip install python-dotenv
pip install openai
```

Or install everything together:

```bash
pip install langchain langchain-openai python-dotenv openai
```

---

## Environment Variables

Create a `.env` file in the project directory.

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
```

---

## Dependencies

```text
langchain
langchain-openai
python-dotenv
openai
```

---

