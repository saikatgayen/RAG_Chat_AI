# PDF_CHAT_AI (RAG v1 – Chunked Retrieval, Local LLM)

A **Retrieval-Augmented Generation (RAG) v1 project** that lets users chat with any PDF document using a locally hosted LLM (Ollama + LLaMA3).

This version upgrades the naive approach by introducing **text chunking and retrieval**, ensuring that only **relevant parts of the document** are sent to the model for each query.

The project is built as a **CLI-based learning-first system**, focusing on understanding *how RAG works internally* before adding embeddings, vector databases, or APIs.

---

## Project Overview

The application performs the following steps:

1. User selects a PDF file at runtime
2. Text is extracted from the PDF
3. The document is split into overlapping chunks
4. For each user question:

   * Relevant chunks are selected using keyword-based scoring
   * Only those chunks are passed as context to the LLM
5. The LLM answers **strictly from the retrieved document context**

If the information is not present in the document, the model is instructed to say so.

---

## What This Version Demonstrates

* Why sending the entire document to an LLM is inefficient
* How **chunking** improves focus and reduces token usage
* What “retrieval” means *before* embeddings are introduced
* How RAG systems evolve incrementally

This represents **RAG v1: Chunked Retrieval (No Embeddings)**.

---

## Project Structure

```
pdf_chat_basic/
├── pdf_chat.py          # CLI-based RAG pipeline (v1)
├── data/
│   └── sample.pdf       # Example PDF (optional)
├── requirements.txt     # Dependencies
└── README.md
```

---

## Tech Stack

* **Python**
* **Ollama** (local LLM runtime)
* **LLaMA3** (language model)
* **PyPDF** (PDF text extraction)

No cloud APIs, no vector databases, and no web frameworks are used.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/PDF_CHAT_AI.git
cd PDF_CHAT_AI
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and configure Ollama

* Download Ollama from: [https://ollama.com](https://ollama.com)
* Pull the model:

```bash
ollama pull llama3
```

---

## Usage

Run the application:

```bash
python pdf_chat.py
```

You will be prompted to enter the path to a PDF file:

```
Enter path to PDF file: /path/to/your/document.pdf
```

Ask questions in the terminal. Type `exit` to quit.

---

## Example Questions

* "What is this document about?"
* "Explain the concept of X mentioned in the PDF"
* "What does the document say about Y?"

The model responds using **only the retrieved chunks** from the PDF.

---

## Known Limitations

This version uses **keyword-based retrieval**, which has limitations:

* Does not understand synonyms or semantic similarity
* Retrieval quality depends on exact word overlap
* Not optimal for very large or complex documents

These limitations are intentional and motivate the next upgrade.

---

## Planned Improvements

Future versions will include:

* Semantic retrieval using embeddings
* Vector search with FAISS
* Better chunk metadata (page numbers, sources)
* Modular project structure
* Optional FastAPI interface

---

## Learning Outcomes

By building this version, you gain hands-on understanding of:

* Core RAG concepts
* Chunking strategies and trade-offs
* Retrieval logic without abstractions
* How LLM context grounding works

---

## License

This project is intended for educational purposes.

---

## 👤 Author

**Saikat Gayen**

Aspiring AI / LLM Engineer | Python | RAG Systems |
