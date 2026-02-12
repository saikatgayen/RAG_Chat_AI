PDF_CHAT_AI (RAG v2 – Semantic Search with Embeddings, Local LLM)

A Retrieval-Augmented Generation (RAG) v2 project that allows users to chat with any PDF document using a locally hosted LLM (Ollama + LLaMA3) and embedding-based semantic search.

This version upgrades the previous keyword-based retrieval system by introducing:

- Sentence-aware chunking

- Embedding generation using Sentence Transformers

- Cosine similarity–based semantic retrieval

The system now retrieves context based on meaning, not just word overlap.

The project remains CLI-based and learning-focused, designed to deeply understand how modern RAG systems work internally before introducing vector databases or production APIs.

 Project Evolution
 RAG v0 – Naive Approach

- The entire PDF was sent to the LLM

- Inefficient and not scalable

 RAG v1 – Chunked Keyword Retrieval

- Document split into chunks

- Chunks selected using word overlap scoring

- Improved token efficiency

- Limited semantic understanding

 RAG v2 – Semantic Retrieval (Current Version)

- Sentence-aware overlapping chunks

- Embeddings generated using all-MiniLM-L6-v2

- Cosine similarity for retrieval

- Top-k semantically relevant chunks sent to LLM

This version reflects a real-world RAG pipeline architecture.

What This Version Demonstrates

- How do embeddings represent semantic meaning?

- Why is keyword retrieval insufficient?

- How does cosine similarity enable semantic search?

- How to build a RAG pipeline from scratch (no frameworks)?

- How does retrieval grounding improve LLM reliability?

This is a true embedding-powered RAG system running fully locally.

Architecture Overview

PDF
 ↓
Text Extraction (PyPDF)
 ↓
Sentence-Based Chunking (with overlap)
 ↓
Embedding Generation (Sentence Transformers)
 ↓
Store Chunk Embeddings (in memory)
 ↓
User Question
 ↓
Embed Question
 ↓
Cosine Similarity
 ↓
Top-K Semantic Chunk Retrieval
 ↓
Pass Context to LLaMA3 (Ollama)
 ↓
Grounded Answer

Project Structure

PDF_CHAT_AI/
├── pdf_chat.py          # Full RAG v2 pipeline (CLI-based)
├── data/
│   └── sample.pdf       # Example PDF (optional)
├── requirements.txt
└── README.md
