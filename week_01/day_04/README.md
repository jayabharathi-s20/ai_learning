# Day 04 - Embeddings & Vector Database

## Overview

This folder contains my Day 04 AI learning exercises on Embeddings and Vector Databases using OpenAI Embeddings, LangChain, and PGVector.

As part of this task, I learned how semantic search works by generating vector embeddings for text, storing them in a PostgreSQL database using PGVector, and retrieving the most relevant documents through similarity search. I also implemented a simple Retrieval-Augmented Generation (RAG) workflow by loading PDF documents, generating embeddings, storing them in a vector database, and querying them using natural language.

---

## Project Structure

```text
day_04/
│
├── README.md
├── learnings.md
├── config.py
├── vector_store.py
├── load_documents.py
├── main.py
└── data/
    └── ai_learning.pdf
```

---

## Files

### `learnings.md`

Contains my Day 04 learning notes, including:

- Introduction to Embeddings
- Semantic Search
- OpenAI Embedding Models
- Vector Databases
- PGVector
- Storing Embeddings
- Similarity Search

---

### `config.py`

Stores the project configuration.

The file:

- Loads environment variables from the `.env` file.
- Retrieves the OpenAI API key.
- Configures the PostgreSQL database connection string.

---

### `load_documents.py`

Loads PDF documents for processing.

The program:

- Reads PDF files.
- Extracts text from the documents.
- Splits large documents into smaller chunks for embedding generation.

Run individually:

```bash
python load_documents.py
```

---

### `vector_store.py`

Configures the PGVector vector store.

The program:

- Creates the OpenAI embedding model.
- Connects to the PostgreSQL database.
- Initializes the PGVector vector store.
- Provides the vector store instance for storing and retrieving document embeddings.

---

### `main.py`

Acts as the entry point of the application.

The program:

- Loads PDF documents.
- Generates embeddings using the OpenAI Embeddings model.
- Stores the document embeddings in PGVector.
- Accepts user queries.
- Performs semantic similarity search.
- Retrieves and displays the most relevant document chunks.

Run the application:

```bash
python main.py
```

---

## Installation

Install the required packages:

```bash
pip install langchain
pip install langchain-openai
pip install langchain-community
pip install langchain-postgres
pip install pypdf
pip install "psycopg[binary]"
```

Or install everything together:

```bash
pip install langchain langchain-openai langchain-community langchain-postgres pypdf "psycopg[binary]"
```

---

## Environment Variables

Create a `.env` file in the project directory.

```env
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/vector_db
```

---

## Dependencies

The following packages are used:

```text
langchain
langchain-openai
langchain-community
langchain-postgres
pypdf
psycopg[binary]
```

---

