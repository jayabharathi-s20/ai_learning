# Data Ingestion

A Retrieval-Augmented Generation (RAG) data ingestion pipeline built using **Python**, **LangChain**, **OpenAI Embeddings**, **PostgreSQL**, and **PGVector**.

This application loads documents from multiple file formats, splits them into chunks, generates vector embeddings, and stores them in PostgreSQL using PGVector for semantic search.

---

# Features

- Multi-format document ingestion
- Automatic document loading from a data folder
- Document chunking
- OpenAI embedding generation
- PGVector integration
- Semantic search support
- FastAPI integration
- Automatic ingestion during application startup

---

# Supported File Formats

- PDF
- DOCX
- CSV
- TXT
- XLSX
- PPTX

---

# Project Structure

```
app/
│
├── data/
│   ├── sample.pdf
│   ├── sample.docx
│   ├── sample.csv
│   ├── sample.txt
│   ├── sample.xlsx
│   └── sample.pptx
│
├── config.py
├── loaders.py
├── splitter.py
├── embeddings.py
├── vector_store.py
├── ingest.py
├── retriever.py
├── main.py
├── .env
└── requirements.txt
```

---

# Technologies Used

- Python
- FastAPI
- LangChain
- OpenAI
- PostgreSQL
- PGVector
- SQLAlchemy
- python-dotenv

---

# Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_key

OPENAI_MODEL=gpt-4o-mini
EMBEDDINGS_MODEL=text-embedding-3-small

DB_HOST=localhost
DB_PORT=5432
DB_NAME_RAG=rag_db
DB_USER=postgres
DB_PASSWORD=password

COLLECTION_NAME=knowledge_base

CHUNK_SIZE=500
CHUNK_OVERLAP=100
```

---

# PostgreSQL Setup

Create the database.

```sql
CREATE DATABASE rag_db;
```

Connect to the database.

```bash
psql -U postgres -d rag_db
```

Enable PGVector.

```sql
CREATE EXTENSION vector;
```

Verify.

```sql
\dx
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Add Documents

Place all supported files inside the `data/` folder.

Example:

```
data/
├── report.pdf
├── employees.csv
├── notes.docx
├── presentation.pptx
├── document.txt
└── sales.xlsx
```

The application automatically detects the file type and loads it using the appropriate LangChain loader.

---

# Run the Application

Start the FastAPI server.

```bash
uvicorn main:app --reload
```

---

# Application Flow

When the application starts:

```
FastAPI Starts
        │
        ▼
Application Startup Event
        │
        ▼
Scan data/ Folder
        │
        ▼
Detect File Type
        │
        ▼
Load Documents
        │
        ▼
Convert to LangChain Documents
        │
        ▼
Split into Chunks
        │
        ▼
Generate OpenAI Embeddings
        │
        ▼
Store in PGVector
```

---

# Retrieval Flow

When a user performs semantic search:

```
User Query
      │
      ▼
Generate Query Embedding
      │
      ▼
PGVector Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Return Results
```

---

# API Endpoints

## Automatic Ingestion

Document ingestion runs automatically when the FastAPI application starts.

---

## Manual Ingestion

```
POST /ingest
```

Indexes all supported documents from the `data/` folder.

---

## Semantic Search

```
GET /search
```

Example:

```
/search?query=What is Artificial Intelligence?
```

Response:

```json
{
  "results": [
    {
      "content": "...",
      "metadata": {
        "source": "ai_learning.pdf",
        "file_format": "pdf"
      }
    }
  ]
}
```

---

# Supported LangChain Loaders

| File Type | Loader |
|-----------|--------|
| PDF | PyMuPDFLoader |
| DOCX | Docx2txtLoader |
| CSV | CSVLoader |
| TXT | TextLoader |
| XLSX | UnstructuredExcelLoader |
| PPTX | UnstructuredPowerPointLoader |

---

# Workflow Summary

```
Documents
     │
     ▼
Loaders
     │
     ▼
LangChain Documents
     │
     ▼
RecursiveCharacterTextSplitter
     │
     ▼
Chunks
     │
     ▼
OpenAI Embeddings
     │
     ▼
PGVector
     │
     ▼
Semantic Search
```

---

# Future Enhancements

- LLM Integration
- Complete RAG Pipeline
- Metadata Filtering
- Hybrid Search
- Streaming Responses
- Conversation Memory