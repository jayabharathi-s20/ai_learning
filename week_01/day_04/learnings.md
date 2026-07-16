# Day 04 – Embeddings & Vector Database

## Objective

Learn how semantic search works by generating text embeddings, storing them in a vector database (PGVector), and retrieving the most relevant information using similarity search.

---

# 1. What are Embeddings?

## Definition

Embeddings are numerical vector representations of text that capture its semantic meaning.

Unlike keyword search, embeddings allow computers to understand the meaning and context of words and sentences.

For example:

```text
Sentence 1:
"I love programming."

Sentence 2:
"I enjoy coding."

Keyword Search:
Different words → May not match

Embedding Search:
Similar meaning → High similarity score
```

Instead of storing text as plain strings, an embedding model converts the text into a list of floating-point numbers.

Example:

```text
"Python is easy."

↓

[0.23, -0.45, 0.81, ..., 0.17]
```

Each number represents a feature learned by the embedding model.

---

## Why Do We Need Embeddings?

Traditional search compares exact words.

Example:

```text
Query:
"How to learn Python?"

Document:
"Python programming tutorial."
```

Keyword Search:

- Different words
- Lower matching accuracy

Embedding Search:

- Understands similar meaning
- Returns relevant results

Embeddings help AI systems perform:

- Semantic Search
- Document Retrieval
- Recommendation Systems
- Retrieval-Augmented Generation (RAG)
- Clustering Similar Documents

---

# 2. Generating Embeddings

OpenAI provides embedding models that convert text into vector representations.

Example:

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)
```

### Explanation

#### `OpenAIEmbeddings`

Creates an embedding model object.

#### `model`

Specifies the embedding model.

Example:

```python
model="text-embedding-3-small"
```

This model converts text into dense vector representations suitable for semantic search.

---

## Generating an Embedding

Example:

```python
embedding = embeddings.embed_query(
    "What is Artificial Intelligence?"
)
```

Output:

```text
[
  0.024,
 -0.153,
 0.412,
 ...
]
```

The output is a high-dimensional vector representing the meaning of the input text.

---

# 3. What is a Vector Database?

A vector database stores embeddings instead of plain text.

It allows efficient searching based on semantic similarity rather than exact keyword matching.

Workflow:

```text
Document
      │
      ▼
Generate Embedding
      │
      ▼
Store Vector
      │
      ▼
Vector Database
      │
      ▼
Similarity Search
      │
      ▼
Most Relevant Documents
```

Popular vector databases include:

- PGVector (PostgreSQL Extension)
- Pinecone
- Weaviate
- Chroma
- Milvus

For this project, PGVector is used.

---

# 4. Storing Embeddings in PGVector

PGVector is a PostgreSQL extension that stores vector embeddings and supports similarity search.

Example:

```python
from langchain_postgres import PGVector

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_documents",
    connection=DATABASE_URL,
    use_jsonb=True
)
```

### Explanation

#### `embeddings`

Embedding model used to generate vectors.

#### `collection_name`

Logical collection where document embeddings are stored.

Example:

```python
collection_name="my_documents"
```

#### `connection`

Database connection string.

Example:

```python
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/vector_db
```

#### `use_jsonb=True`

Stores document metadata in PostgreSQL using the JSONB data type for efficient querying.

---

# 5. Loading Documents into the Vector Store

Before searching, documents must be loaded, converted into embeddings, and stored.

Workflow:

```text
PDF Document
      │
      ▼
Read Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in PGVector
```

Each document chunk receives its own embedding, allowing more accurate retrieval of relevant information.

---
# 5.1 Document Chunking

## What is Chunking?

Chunking is the process of splitting a large document into smaller pieces called **chunks** before generating embeddings.

Instead of creating a single embedding for an entire document, embeddings are generated for each chunk.

Example:

```text
Original Document

-------------------------------------
Python is a programming language...

It is widely used in AI...

It also supports web development...

-------------------------------------

↓

Chunk 1

Python is a programming language...

↓

Chunk 2

It is widely used in AI...

↓

Chunk 3

It also supports web development...
```

Each chunk receives its own embedding and is stored separately in the vector database.

---

## Why is Chunking Needed?

Large documents often exceed the embedding model's context limits.

Chunking provides several benefits:

- Produces more accurate embeddings.
- Improves semantic search results.
- Reduces memory usage.
- Retrieves only the most relevant portions of a document.

Without chunking, searching a large document becomes less efficient and less accurate.

---

# 5.2 Chunk Size

## What is Chunk Size?

Chunk size defines the maximum number of characters (or tokens) contained in each chunk.

Example:

```python
chunk_size = 1000
```

This means each chunk contains approximately 1000 characters before being split.

### Small Chunk Size

```text
Chunk Size = 200
```

Advantages:

- More precise search results.
- Better semantic understanding.

Disadvantages:

- Creates many chunks.
- Requires more storage.

---

### Large Chunk Size

```text
Chunk Size = 2000
```

Advantages:

- More context in each chunk.
- Fewer embeddings to store.

Disadvantages:

- Lower retrieval precision.
- May include unrelated information.

---

# 5.3 Chunk Overlap

## What is Chunk Overlap?

Chunk overlap specifies how much content is shared between consecutive chunks.

Example:

```python
chunk_overlap = 200
```

Suppose:

```text
Chunk Size = 1000

Chunk Overlap = 200
```

Then:

```text
Chunk 1

Characters:
1 -------------------1000

Chunk 2

Characters:
801------------------1800
```

The last 200 characters of Chunk 1 are repeated at the beginning of Chunk 2.

---

## Why Use Chunk Overlap?

Without overlap, important information that spans across chunk boundaries may be lost.

Overlap helps:

- Preserve context between chunks.
- Improve retrieval accuracy.
- Reduce information loss.

---

# 5.4 Choosing Chunk Size and Chunk Overlap

Common values used in RAG applications:

```python
chunk_size = 1000
chunk_overlap = 200
```

These values provide a good balance between context preservation and retrieval accuracy.

The optimal values depend on:

- Document size
- Document type
- Embedding model
- Application requirements


# 6. Similarity Search

## What is Similarity Search?

Similarity search compares the embedding of a user's query with stored document embeddings.

Instead of matching keywords, it finds documents with similar meaning.

Example:

```text
Stored Document:
"Python is used for web development."

User Query:
"What can Python be used for?"

↓

Semantic Similarity

↓

Relevant Document Returned
```

---

## Example

```python
results = vector_store.similarity_search(
    "What is Python used for?",
    k=3
)
```

### Explanation

#### `similarity_search()`

Searches the vector database for the most semantically similar documents.

#### `k`

Number of documents to return.

Example:

```python
k=3
```

Returns the top three most relevant document chunks.
---

# 6.1 Understanding `k` in Similarity Search

When performing similarity search:

```python
results = vector_store.similarity_search(
    "What is Python used for?",
    k=3
)
```

### What is `k`?

`k` specifies the number of most similar document chunks to retrieve.

Example:

```python
k=3
```

The vector database returns the **top three** document chunks with the highest semantic similarity to the user's query.

---

### Example

Suppose the vector database contains:

```text
Chunk A
Python is a programming language.

Chunk B
Python is widely used for AI.

Chunk C
Python supports web development.

Chunk D
Java is an object-oriented language.
```

Query:

```text
"What is Python used for?"
```

If:

```python
k = 2
```

Results:

```text
1. Python is widely used for AI.

2. Python supports web development.
```

Only the two most relevant chunks are returned.

---

### Choosing the Right `k`

Small `k`:

```python
k = 1
```

- Faster retrieval.
- Returns only the single most relevant result.

Medium `k`:

```python
k = 3
```

- Balanced amount of context.
- Common choice for RAG systems.

Large `k`:

```python
k = 10
```

- Retrieves more context.
- Increases processing time and token usage.

The value of `k` should be chosen based on the application's retrieval requirements.
---


---

# 7. End-to-End Workflow

```text
PDF Documents
        │
        ▼
Load Documents
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
        ▼
User Query
        │
        ▼
Generate Query Embedding
        │
        ▼
Similarity Search
        │
        ▼
Retrieve Relevant Documents
```

---

# Why Use a Vector Database?

Vector databases provide:

- Fast semantic search
- Better search accuracy
- Efficient retrieval of similar documents
- Scalable storage for AI applications
- Foundation for Retrieval-Augmented Generation (RAG)

---

# Key Learnings

- Learned what embeddings are and how they represent the semantic meaning of text.
- Understood the difference between keyword search and semantic search.
- Generated embeddings using OpenAI's `text-embedding-3-small` model.
- Learned how vector databases store embeddings instead of plain text.
- Configured and used PGVector with PostgreSQL to store document embeddings.
- Understood the role of `collection_name`, `connection`, and metadata storage using JSONB.
- Learned the complete document indexing workflow, from loading documents to storing embeddings.
- Performed similarity search to retrieve the most relevant documents based on semantic meaning.
- Understood how embeddings and vector databases form the foundation of Retrieval-Augmented Generation (RAG) applications.

---

# Outcome

By the end of Day 04, I am able to:

- Explain what embeddings are and why they are used in AI applications.
- Generate text embeddings using OpenAI embedding models.
- Store document embeddings in PGVector.
- Perform semantic similarity search on stored documents.
- Build the core retrieval pipeline required for RAG-based AI applications.