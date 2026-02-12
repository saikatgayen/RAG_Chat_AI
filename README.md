PDF_CHAT_AI (RAG v2 – Embeddings + Semantic Search, Local LLM)

A Retrieval-Augmented Generation (RAG) v2 project that allows users to chat with any PDF document using a locally hosted LLM (Ollama + LLaMA3) combined with semantic search via embeddings.

This version upgrades RAG v1 by replacing keyword-based retrieval with embedding-based semantic similarity, enabling the system to understand paraphrasing, synonyms, and conceptual similarity.

The project remains CLI-based and learning-focused, designed to clearly demonstrate how modern RAG systems work internally before introducing vector databases or production infrastructure.

🚀 Project Overview

The application performs the following pipeline:

User selects a PDF file at runtime

Text is extracted from the PDF

The document is split into overlapping sentence-aware chunks

Each chunk is converted into a vector embedding

For each user question:

The question is embedded

Cosine similarity is computed against all chunk embeddings

Top-k most semantically relevant chunks are retrieved

Only those relevant chunks are passed as context to the LLM

The LLM answers strictly from the retrieved context

If the answer is not present in the document, the model is instructed to say:

"Not found in the document."

🧠 What This Version Demonstrates

This represents RAG v2: Semantic Retrieval with Embeddings.

You will understand:

Why keyword matching is limited

How embeddings represent semantic meaning

How cosine similarity enables semantic search

How modern RAG systems retrieve relevant context

The mathematical foundation behind vector-based retrieval

This version moves closer to industry-standard RAG architecture.

🏗️ Architecture Flow
PDF
 ↓
Text Extraction (PyPDF)
 ↓
Sentence-Aware Chunking (with overlap)
 ↓
Embedding Generation (SentenceTransformers)
 ↓
Store Chunk Embeddings (in memory)
 ↓
User Question
 ↓
Embed Question
 ↓
Cosine Similarity Search
 ↓
Top-K Relevant Chunks
 ↓
Pass Context to LLaMA3 (Ollama)
 ↓
Grounded Answer

📁 Project Structure
PDF_CHAT_AI/
├── pdf_chat.py          # CLI-based RAG v2 pipeline
├── data/
│   └── sample.pdf       # Example PDF (optional)
├── requirements.txt     # Dependencies
└── README.md

⚙️ Tech Stack

Python

Ollama (local LLM runtime)

LLaMA3 (language model)

PyPDF (PDF text extraction)

SentenceTransformers (embeddings)

NumPy (vector math / cosine similarity)

No cloud APIs, no external vector databases.

Everything runs locally.

📦 Installation
1. Clone the repository
git clone https://github.com/<your-username>/PDF_CHAT_AI.git
cd PDF_CHAT_AI

2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt


Make sure requirements.txt includes:

pypdf
ollama
sentence-transformers
numpy

4. Install and configure Ollama

Download from:
https://ollama.com

Pull the model:

ollama pull llama3

▶️ Usage

Run the application:

python pdf_chat.py


You will be prompted:

Enter the path to your PDF file:


Then ask questions in the terminal.

Type exit to quit.

📝 Example Questions

"What is this document about?"

"Explain the main idea in simple terms."

"What does the paper say about neural architectures?"

"Summarize the section discussing model evaluation."

Unlike RAG v1, this version can handle:

Synonyms

Paraphrased questions

Conceptual similarity

Indirect phrasing

🔍 Why RAG v2 Is Better Than RAG v1
Feature	RAG v1	RAG v2
Keyword Matching	✅	❌
Semantic Understanding	❌	✅
Handles Synonyms	❌	✅
Cosine Similarity	❌	✅
Embeddings	❌	✅
Industry Relevance	Basic	Practical

RAG v2 uses vector embeddings + cosine similarity, which is how most production RAG systems begin.

⚠️ Current Limitations

Embeddings are recomputed every run (not persisted)

Retrieval is in-memory (no FAISS / vector DB yet)

No page-number citation

CLI-only interface

These limitations are intentional for learning clarity.

🔮 Planned Improvements (Next Versions)

Future upgrades may include:

Persistent embedding storage

FAISS for scalable vector search

Metadata tracking (page numbers, source citations)

Modular RAG architecture

Streaming responses

FastAPI / Web UI

Multi-document support

🎯 Learning Outcomes

By building this version, you gain hands-on understanding of:

Embedding models

Vector representations of text

Cosine similarity mathematics

Semantic search fundamentals

Real RAG architecture

Context grounding techniques

This is a strong foundation for:

LLM engineering roles

Applied AI roles

RAG system development

Production LLM pipelines

📜 License

This project is intended for educational and learning purposes.

👤 Author

Saikat Gayen

Aspiring AI / LLM Engineer
Python | RAG Systems | Local LLMs | Semantic Search
