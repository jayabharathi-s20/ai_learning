# 📚 RAG Pipeline using LangChain, FastAPI & PGVector

A Retrieval-Augmented Generation (RAG) application built with **FastAPI**, **LangChain**, **OpenAI Embeddings**, and **PGVector**. This project indexes PDF documents into a PostgreSQL vector database and answers user questions using relevant document context.

---

# Features

- Load PDF documents
- Split documents into chunks
- Generate OpenAI embeddings
- Store embeddings in PostgreSQL (PGVector)
- Retrieve relevant chunks using semantic search
- Generate context-aware answers using GPT-4o Mini
- REST APIs using FastAPI
- Interactive Swagger documentation

---

# Project Structure

```
app/
│
├── config.py              # Environment variables & configuration
├── loader.py              # PDF loading and text chunking
├── create_embeddings.py   # OpenAI Embeddings & PGVector setup
├── retriever.py           # Vector retriever
├── rag_pipeline.py        # Index PDF into vector database
├── main.py                # FastAPI application
├── __init__.py
│
└── data/
    └── ai_learning.pdf

.env
requirements.txt
README.md
```

---

# Technologies Used

- Python 3.12
- FastAPI
- LangChain
- OpenAI
- PostgreSQL
- PGVector
- PyMuPDF
- Uvicorn

---

# Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create a PostgreSQL database.

```sql
CREATE DATABASE vector_db;
```

Enable the PGVector extension.

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key

OPENAI_MODEL=gpt-4o-mini
EMBEDDINGS_MODEL=text-embedding-3-small

DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME_RAG_CHAIN=vector_db

COLLECTION_NAME=python_docs

CHUNK_SIZE=500
CHUNK_OVERLAP=100
```

---

# Running the Application

Start the FastAPI server.

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## GET /

Checks whether the application is running.

**Response**

```json
{
  "message": "RAG API is running"
}
```

---

## POST /index

Indexes the PDF located at:

```
app/data/ai_learning.pdf
```

This endpoint:

- Loads the PDF
- Splits the content into chunks
- Generates embeddings
- Stores embeddings in PGVector

**Response**

```json
{
  "message": "PDF indexed successfully",
  "chunks_indexed": 18
}
```

---

## POST /ask

Retrieves relevant document chunks and generates an answer.

**Request**

```json
{
  "question": "What is Prompt Engineering?"
}
```

**Response**

```json
{
  "question": "What is Prompt Engineering?",
  "answer": "Prompt Engineering is..."
}
```

---

# RAG Workflow

```
PDF
 │
 ▼
Load PDF
 │
 ▼
Split into Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Store in PGVector
 │
────────────────────────────────

User Question
 │
 ▼
Convert Question to Embedding
 │
 ▼
Similarity Search
 │
 ▼
Retrieve Relevant Chunks
 │
 ▼
GPT-4o Mini
 │
 ▼
Generate Answer
```

---

# Components

### `config.py`

Loads configuration values from the `.env` file.

### `loader.py`

Loads the PDF using PyMuPDF and splits it into smaller chunks.

### `create_embeddings.py`

Initializes the OpenAI embedding model and PGVector vector store.

### `retriever.py`

Creates a retriever to perform semantic similarity search.

### `rag_pipeline.py`

Processes the PDF and stores its embeddings in PostgreSQL.

### `main.py`

Implements the FastAPI application and exposes the following endpoints:

- `/index`
- `/ask`

---
