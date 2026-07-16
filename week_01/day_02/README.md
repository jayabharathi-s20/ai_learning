# Day 02 - Prompt Engineering

## Overview

This folder contains my Day 02 AI learning exercises on Prompt Engineering using the OpenAI Python SDK.

As part of this task, I learned different prompt engineering techniques, documented my learnings, and implemented practical Python examples to understand how prompts influence LLM responses.

---

## Project Structure

```text
day_02/
│
├── README.md
├── learnings.md
├── requirements.txt
├── zero_shot_prompting.py
├── few_shot_prompting.py
└── prompt_engineering.py
```

---

## Files

### `learnings.md`

Contains my Day 02 learning notes, including:

- Prompt Engineering
- Controlling LLM Outputs
- Structured Prompts
- Role-Based Prompting
- Output Formatting
- Zero-Shot Prompting
- Few-Shot Prompting

---

### `zero_shot_prompting.py`

Implements **Zero-Shot Prompting**, where the model performs a task without being provided any examples.

Run this file to observe how the LLM completes a task using only the given instruction.

Run the Zero-Shot Prompting example:

```bash
python zero_shot_prompting.py
```

---

### `few_shot_prompting.py`

Implements **Few-Shot Prompting**, where a few examples are provided before asking the model to perform the same task.

Run this file to compare its behavior with Zero-Shot Prompting.

```bash
python few_shot_prompting.py
```

---

### `prompt_engineering.py`

Implements the Day 02 prompt engineering concepts by combining:

- Structured Prompt
- Role-Based Prompting
- Output Formatting
- Response Constraints

The program accepts user input and generates a structured response based on the prompt design.

Run this file :

```bash
python prompt_engineering.py
```

---

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

## Outcome

By completing this task, I gained hands-on experience with:

- Writing effective prompts
- Implementing Zero-Shot Prompting
- Implementing Few-Shot Prompting
- Designing structured prompts
- Applying role-based prompting
- Formatting LLM responses
- Controlling model outputs using prompt instructions