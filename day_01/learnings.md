# Week 4 – LLMs, Prompting & Embeddings

## Table of Contents

1. What is an LLM?
2. What is Prompting?
3. What is Embedding?
4. How LLMs Work
5. Understanding Tokens
6. Understanding Token Cost
7. Zero-Shot Prompting
8. Few-Shot Prompting
9. Summary

---

# 1. What is an LLM?

## Definition

**LLM (Large Language Model)** is an Artificial Intelligence (AI) model trained on massive amounts of text data such as books, websites, articles, research papers, and source code. It learns language patterns and uses those patterns to understand and generate human-like text.

An LLM can:

- Answer questions
- Generate code
- Summarize documents
- Translate languages
- Write emails
- Analyze text
- Generate reports
- Assist in conversations

## Examples of LLMs

- GPT (ChatGPT)
- Claude
- Gemini
- Llama
- Mistral

## LLM Workflow

```text
Training Data
(Books, Websites, Code)
        │
        ▼
Large Language Model
        │
        ▼
Learns Language Patterns
        │
        ▼
Generates Human-like Responses
```

### Example

**Prompt**

```
Explain JWT Authentication.
```

**Response**

The LLM understands the question and generates a detailed explanation.

---

# 2. What is Prompting?

## Definition

A **Prompt** is the instruction, question, or context given to an LLM.

**Prompting** is the process of communicating with an LLM to obtain the desired output.

Simply put,

> Prompt = Input given to the AI

> Prompting = The process of interacting with the AI using prompts.

---

## Prompt Workflow

```text
User Prompt
      │
      ▼
Large Language Model
      │
      ▼
Generated Response
```

### Example

**Prompt**

```
Write a FastAPI API to create a new user.
```

The LLM generates the API code.

---

## Good Prompt Example

```
Explain REST API in simple terms with an example suitable for beginners.
```

This prompt provides clear instructions and context, resulting in a better response.

---

# 3. What is Embedding?

## Definition

Embedding is the process of converting text into numerical vectors that capture its meaning.

These vectors enable AI systems to compare the similarity between different pieces of text.

Unlike an LLM, which generates text, embeddings are primarily used for searching and retrieving relevant information.

---

## Embedding Workflow

```text
Text
 │
 ▼
Embedding Model
 │
 ▼
Vector Representation
 │
 ▼
Stored in Vector Database
 │
 ▼
Semantic Search
 │
 ▼
Most Relevant Results
```

---

## Example

Stored documents:

```
Python Developer

Java Developer

Backend Engineer

Frontend Engineer
```

User searches:

```
Python Backend Engineer
```

Embedding compares meanings instead of exact words.

Possible similarity:

```
Python Developer → 96%

Backend Engineer → 93%

Java Developer → 48%

Frontend Engineer → 25%
```

---

## Applications of Embeddings

- Semantic Search
- Recommendation Systems
- Retrieval-Augmented Generation (RAG)
- Document Retrieval
- Similarity Search
- Duplicate Detection

---

# 4. How LLMs Work

LLMs go through two major phases:

1. **Training Phase** – The model learns language patterns from massive datasets.
2. **Inference Phase** – The trained model generates responses to user prompts.

## End-to-End LLM Flow

```text
                TRAINING PHASE

        Massive Text Dataset
                 │
                 ▼
        Data Preprocessing
                 │
                 ▼
          Tokenization
                 │
                 ▼
          Word Embeddings
                 │
                 ▼
     Transformer Neural Network
        (Self-Attention Layers)
                 │
                 ▼
      Predict Next Token
                 │
                 ▼
         Calculate Loss
                 │
                 ▼
        Backpropagation
                 │
                 ▼
      Update Model Parameters
                 │
                 ▼
          Fine-Tuning

                INFERENCE PHASE

      User Prompt
            │
            ▼
      Tokenization
            │
            ▼
      Embeddings
            │
            ▼
 Transformer + Self-Attention
            │
            ▼
 Predict Next Token
            │
            ▼
 Repeat Token Prediction
            │
            ▼
    Final Response
```

## Explanation

1. **Data Collection** – The model is trained using books, websites, documentation, research papers, and source code.
2. **Data Preprocessing** – The text is cleaned, filtered, and prepared for training.
3. **Tokenization** – Text is split into tokens (words, subwords, or punctuation).
4. **Embeddings** – Tokens are converted into numerical vectors that capture semantic meaning.
5. **Transformer & Self-Attention** – The model analyzes relationships between all tokens in the input and understands context.
6. **Next Token Prediction** – During training, the model repeatedly predicts the next token.
7. **Loss Calculation & Backpropagation** – Prediction errors are measured, and model parameters are updated to improve future predictions.
8. **Fine-Tuning** – The base model is further trained to better follow instructions and produce helpful responses.
9. **Inference** – When a user asks a question, the trained model tokenizes the prompt, processes it through the transformer, and generates the response one token at a time.

## Example

Input:

```
Python is a ______ programming language.
```

Prediction:

```
high-level
```

The model continues predicting one token after another until the complete response is generated.

---
# 5. Understanding Tokens

## Definition

A **Token** is the smallest unit of text processed by an LLM.

A token may represent:

- A complete word
- Part of a word
- A punctuation mark
- A number

---

## Example

Sentence:

```
I love Python programming.
```

Possible tokens:

```
I

love

Python

programming

.
```

Another example:

```
unbelievable
```

May become:

```
un

believ

able
```

Different LLMs use different tokenization techniques.

---

## Why Tokens Matter

Every prompt and every response are converted into tokens.

LLMs process tokens—not words.

---

# 6. Understanding Token Cost

LLM APIs charge based on the total number of tokens processed.

Total Tokens =

```
Input Tokens + Output Tokens
```

---

## Example

Prompt:

```
Summarize this document.
```

Input:

```
100 Tokens
```

Response:

```
350 Tokens
```

Total:

```
450 Tokens
```

The API billing is based on the combined token count.

---

## Real Example

Prompt:

```
Analyze this Pull Request and provide feedback.
```

Input:

```
250 Tokens
```

Output:

```
600 Tokens
```

Total:

```
850 Tokens
```

---

# 7. Zero-Shot Prompting

## Definition

Zero-shot prompting means asking the LLM to perform a task **without providing any examples**.

The model relies solely on its training.

---

## Example

Prompt:

```
Translate this sentence into Tamil.

I am learning AI.
```

The LLM translates the sentence directly.

---

## Zero-Shot Flow

```text
Instruction
      │
      ▼
Large Language Model
      │
      ▼
Generated Response
```

---

## Advantages

- Simple
- Fast
- Easy to write

---

# 8. Few-Shot Prompting

## Definition

Few-shot prompting provides one or more examples before asking the model to perform the task.

The examples help the model understand the expected format and style.

---

## Example

Prompt

```
English: Hello
Tamil: வணக்கம்

English: Thank you
Tamil: நன்றி

English: Good Morning
Tamil:
```

Response

```
காலை வணக்கம்
```

---

## Few-Shot Flow

```text
Examples
      │
      ▼
Large Language Model
      │
      ▼
Learns Pattern
      │
      ▼
New Input
      │
      ▼
Generated Response
```

---

## Advantages

- Better accuracy
- Consistent formatting
- Better understanding of user expectations

---

# Zero-Shot vs Few-Shot

| Zero-Shot | Few-Shot |
|------------|-----------|
| No examples are provided. | One or more examples are provided. |
| Simpler prompts. | Better guidance through examples. |
| Faster to write. | More consistent outputs. |
| Relies entirely on model knowledge. | Learns from provided examples. |

---


# 10. Video Learnings

This section summarizes the key concepts learned from the introductory Generative AI videos.

---

## What is Generative AI?

**Generative AI (GenAI)** is a type of Artificial Intelligence that can generate new content based on user prompts. Instead of only analyzing existing data, it can create new outputs such as text, images, code, audio, and videos.

### Examples

- ChatGPT – Generates text and answers questions.
- GitHub Copilot – Generates code.
- DALL·E – Generates images.
- Gemini – Generates text, code, and images.
- Claude – Assists with writing, analysis, and coding.

### How Generative AI Works

```text
User Prompt
      │
      ▼
Large Language Model (LLM)
      │
      ▼
Generated Content
(Text, Code, Images, etc.)
```


---

## What is Supervised Learning?

### Definition

Supervised Learning is a machine learning technique where the model learns from **labeled data**.

Each training example contains:

- Input
- Correct Output (Label)

The model learns the relationship between inputs and outputs.

### Workflow

```text
Labeled Dataset
(Input + Correct Output)
            │
            ▼
Machine Learning Model
            │
            ▼
Learns Pattern
            │
            ▼
Predicts Output for New Data
```

### Example

Training Data

| Email | Label |
|--------|-------|
| Win ₹1,00,000 Now | Spam |
| Meeting at 5 PM | Not Spam |

After training:

Input:

```
Congratulations! Claim your reward.
```

Prediction:

```
Spam
```

### Applications

- Email Spam Detection
- Image Classification
- Disease Prediction
- Fraud Detection
- House Price Prediction

---

## What is Unsupervised Learning?

### Definition

Unsupervised Learning learns from **unlabeled data**.

There are no correct answers provided.

Instead, the model identifies hidden patterns and relationships within the data.

### Workflow

```text
Unlabeled Data
        │
        ▼
Machine Learning Model
        │
        ▼
Finds Hidden Patterns
        │
        ▼
Creates Groups (Clusters)
```

### Example

Customer purchase data:

```
Customer A
Customer B
Customer C
Customer D
```

The algorithm automatically groups similar customers based on their purchasing behavior.

Possible result:

```
Cluster 1 → Frequent Buyers

Cluster 2 → Occasional Buyers

Cluster 3 → New Customers
```

### Applications

- Customer Segmentation
- Recommendation Systems
- Pattern Discovery
- Anomaly Detection

---

## What is Reinforcement Learning?

### Definition

Reinforcement Learning (RL) is a learning technique where an AI agent learns by interacting with an environment.

The agent receives:

- Rewards for correct actions
- Penalties for incorrect actions

Its objective is to maximize the total reward over time.

### Workflow

```text
Environment
      │
      ▼
AI Agent
      │
Choose Action
      │
      ▼
Reward / Penalty
      │
      ▼
Learns Better Strategy
```

### Example

Teaching a Robot

```
Robot walks correctly
        ↓
Reward +10

Robot falls
        ↓
Penalty -5

Robot learns to balance better over time.
```

### Applications

- Robotics
- Self-driving Cars
- Game Playing (Chess, Go)
- Autonomous Systems
- Resource Optimization

---

## Difference Between Learning Types

| Feature | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|----------|---------------------|-----------------------|------------------------|
| Training Data | Labeled | Unlabeled | Reward-Based |
| Goal | Predict Correct Output | Discover Hidden Patterns | Learn Optimal Actions |
| Feedback | Correct Labels | No Labels | Rewards & Penalties |
| Example | Spam Detection | Customer Segmentation | Robot Learning |

---

## Relationship Between GenAI and Machine Learning

```text
Artificial Intelligence (AI)
        │
        ▼
Machine Learning (ML)
        │
        ├───────────────┐
        │               │
        ▼               ▼
Supervised      Unsupervised
Learning         Learning
        │
        ▼
Deep Learning
        │
        ▼
Large Language Models (LLMs)
        │
        ▼
Generative AI
(ChatGPT, Claude, Gemini, etc.)
```

---

## Key Learnings

- Generative AI creates new content such as text, code, images, and audio.
- LLMs are the foundation of modern Generative AI applications.
- Supervised Learning uses labeled data to learn patterns.
- Unsupervised Learning discovers hidden structures in unlabeled data.
- Reinforcement Learning learns through rewards and penalties.
- AI is a General Purpose Technology that can improve productivity across many industries.
- Understanding these concepts forms the foundation for learning advanced Generative AI topics.