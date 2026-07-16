# Day 03 - OpenAI API

## Overview

This folder contains my Day 03 AI learning exercises on using the OpenAI API with the OpenAI Python SDK.

As part of this task, I learned how to integrate Large Language Models (LLMs) into Python applications by making API calls, tuning model parameters, and calculating API usage costs. I also implemented practical Python examples to understand how to build conversational applications, customize model behavior, and estimate token-based pricing.

---

## Project Structure

```text
day_03/
│
├── README.md
├── learnings.md
├── api_calling.py
├── tune_parameters.py
└── costs.py
```

---

## Files

### `learnings.md`

Contains my Day 03 learning notes, including:

- OpenAI API Fundamentals
- Calling the OpenAI API
- Chat Completions API
- Understanding API Request & Response
- Model Parameters
- Token Usage
- Usage Cost Calculation
- Integrating LLMs into Applications

---

### `api_calling.py`

Implements a conversational chatbot using the Chat Completions API.

The program:

- Loads the OpenAI API key from the `.env` file.
- Maintains conversation history using the `messages` list.
- Sends user prompts to the OpenAI API.
- Receives and displays AI-generated responses.
- Supports continuous conversation until the user exits.

Run the chatbot:

```bash
python api_calling.py
```

---

### `tune_parameters.py`

Demonstrates how different model parameters influence the behavior of the LLM.

The implementation explores parameters such as:

- Model Selection
- Temperature
- Max Completion Tokens
- Top-p
- Frequency Penalty
- Presence Penalty

Run the parameter tuning example:

```bash
python tune_parameters.py
```

---

### `costs.py`

Demonstrates how to retrieve token usage from the API response and estimate the API cost based on the selected model's pricing.

The program:

- Sends a prompt to the model.
- Displays the AI response.
- Retrieves:
  - Prompt Tokens
  - Completion Tokens
  - Total Tokens
- Calculates:
  - Input Cost
  - Output Cost
  - Total Estimated Cost

Run the cost calculation example:

```bash
python costs.py
```

---

## Installation

Install the required packages:

```bash
pip install openai python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Dependencies

The following packages are used:

```text
openai==2.4.0
python-dotenv==1.1.1
```

---

## Concepts Covered

- OpenAI Python SDK
- Chat Completions API
- API Authentication
- Request and Response Handling
- Conversation History
- Model Parameter Tuning
- Token Usage
- API Pricing
- Cost Estimation

---
