# Day 2: Prompt Engineering

## Objective

Learn how to control Large Language Model (LLM) outputs effectively by writing clear, structured, and specific prompts.

---

# What is Prompt Engineering?

Prompt Engineering is the practice of designing effective prompts (instructions) to guide a Large Language Model (LLM) to generate accurate, relevant, and consistent responses.

A **prompt** is simply the input or instruction you provide to an AI model.

## Simple Prompt

```text
Explain Python.
```

Possible Output

```text
Python is a programming language.
```

The response is correct but generic.

---

## Better Prompt

```text
Explain Python to a beginner.

Requirements:
- Use simple English.
- Keep the explanation under 100 words.
- Include one real-world example.
```

Possible Output

```text
Python is a beginner-friendly programming language used to build websites, automate tasks, and analyze data.

Example:
Python can automatically organize files on your computer.
```

The second prompt provides more context and constraints, resulting in a better response.

---

# Why is Prompt Engineering Important?

LLMs don't automatically know exactly what you want. They generate responses based on the instructions you provide.

A well-written prompt helps the model produce responses that are:

- Accurate
- Relevant
- Consistent
- Well-structured
- Easy to understand

---

# Controlling LLM Outputs Effectively

"Controlling LLM outputs" means guiding the AI to generate responses that match your expectations.

Instead of asking:

```text
Explain AI.
```

Ask:

```text
Explain Artificial Intelligence.

Requirements:
- Use beginner-friendly language.
- Keep the answer under 100 words.
- Give one real-world example.
- Return the answer as bullet points.
```

Now the model knows:

- What to explain
- Who the audience is
- How long the answer should be
- Which format to use

---

# Techniques to Control LLM Outputs

## 1. Be Specific

Poor Prompt

```text
Explain Java.
```

Better Prompt

```text
Explain Java to a beginner in less than 100 words.
```

---

## 2. Specify the Audience

```text
Explain REST API to a beginner.
```

```text
Explain REST API to an experienced backend developer.
```

The responses will differ because the audience changes.

---

## 3. Add Constraints

Example

```text
Explain Python.

Requirements:
- Maximum 50 words
- Use simple English
- No technical jargon
```

Constraints help control:

- Length
- Tone
- Complexity
- Style

---

## 4. Provide Context

Without Context

```text
Write an email.
```

With Context

```text
Write a professional leave request email for one day because of a medical appointment.
```

Context helps the model generate more relevant responses.

---

## 5. Give Examples (Few-Shot Prompting)

Examples teach the model the desired pattern.

```text
English: Hello
French: Bonjour

English: Thank you
French: Merci

English: Good Night
French:
```

---

# Structure Prompts

A structured prompt helps the model understand exactly what you need.

## Prompt Structure

```
Task
Context
Requirements
Output Format
```

---

## Example

```text
Task:
Explain Python.

Context:
The audience is a beginner.

Requirements:
- Use simple English.
- Less than 100 words.
- Include one example.

Output Format:
Bullet points.
```

---

## Benefits

- Clear instructions
- Better responses
- Less ambiguity
- More consistent output

---

# Role-Based Prompting

Role-based prompting means assigning a role to the model before asking your question.

Instead of simply asking a question, tell the model **who it should act as**.

---

## Example 1 - Python Instructor

```text
You are an experienced Python instructor.

Explain Python functions to a beginner.
```

---

## Example 2 - Technical Interviewer

```text
You are a technical interviewer.

Ask me five Python interview questions.
```

---

## Example 3 - Senior Software Engineer

```text
You are a senior software engineer.

Review the following Python code and suggest improvements.
```

---

## Example 4 - Career Mentor

```text
You are a career mentor.

Suggest a roadmap to become a Python Full Stack Developer.
```

---

## Benefits

- Domain-specific answers
- Better explanations
- Appropriate tone
- Professional responses

---

# Format Outputs

You can tell the model exactly how you want the response to look.

---

## Bullet Points

```text
Explain REST API.

Return the answer as bullet points.
```

---

## Numbered List

```text
Explain how to install Python.

Return the answer as a numbered list.
```

---

## Markdown Table

```text
Compare Python and Java.

Return the answer as a Markdown table.
```

Example

| Feature | Python | Java |
|---------|---------|------|
| Syntax | Easy | Verbose |
| Typing | Dynamic | Static |
| Learning | Beginner-friendly | Moderate |

---

## JSON

```text
Provide employee information.

Return the response in JSON format.
```

Example

```json
{
  "name": "John",
  "age": 25,
  "department": "IT"
}
```

---

## HTML

```text
Create a login page.

Return only HTML code.
```

---

## Markdown

```text
Explain Machine Learning.

Return the response in Markdown format.
```

---

## Python Code

```text
Write a Python program to check whether a number is prime.

Return only Python code.
```

---

# Best Practices

- Write clear and specific prompts.
- Include enough context.
- Define the audience.
- Add constraints when needed.
- Specify the desired output format.
- Use role-based prompting for specialized responses.
- Use few-shot prompting when consistency is important.

---

# Key Takeaways

- Prompt Engineering is the process of designing effective prompts for LLMs.
- Better prompts produce better responses.
- Structured prompts reduce ambiguity.
- Role-based prompting changes the expertise and tone of the response.
- Output formatting makes responses easier to read and process.
- Zero-shot prompting uses no examples, while few-shot prompting provides examples to guide the model.
- Combining these techniques helps you control LLM outputs more effectively.