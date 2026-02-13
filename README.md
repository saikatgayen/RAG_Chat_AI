# PDF_CHAT_AI
## RAG v2 – Embedding-Based Semantic Retrieval with Local LLM

A Retrieval-Augmented Generation (RAG) v2 project that enables users to chat with any PDF document using a locally hosted LLM (Ollama + LLaMA3) and embedding-based semantic search.

This version upgrades the earlier keyword-based retrieval system by introducing:

 - Sentence-aware overlapping chunking

 - Embedding generation using Sentence Transformers

 - Cosine similarity–based semantic retrieval

The system now retrieves context based on semantic meaning, not just word overlap.

This project remains a CLI-based, learning-first implementation, designed to deeply understand how modern RAG systems work internally before introducing vector databases or APIs.

# Project Overview

The application performs the following steps:

1. User selects a PDF file at runtime

2. Text is extracted from the PDF

3. The document is split into sentence-aware overlapping chunks

4. Embeddings are generated for each chunk

5. For each user question:

    - The question is embedded

    - Cosine similarity is computed against chunk embeddings

    - Top-k semantically relevant chunks are retrieved

    - Only relevant chunks are passed to the LLM

6. The LLM answers strictly from the retrieved context

If the information is not present in the document, the model is instructed to say so explicitly.

# What This Version Demonstrates

 - Why is keyword retrieval limited?

 - How embeddings capture semantic meaning

 - How cosine similarity enables semantic search

 - How a real RAG pipeline is structured

 - How retrieval grounding improves LLM reliability

This represents RAG v2: Embedding-Based Semantic Retrieval.

# Project Structure

<img width="647" height="222" alt="Screenshot 2026-02-13 at 12 26 00" src="https://github.com/user-attachments/assets/e90b6eb7-c565-4064-b1c5-287381a9730e" />

# Tech Stack
 - Python
 - Ollama (local LLM runtime)
 - LLaMA3
 - PyPDF
 - Sentence Transformers
 - NumPy

### Not yet implemented:
 -  **Cloud APIs**
 -  **OpenAI API**
 -  **External vector databases**
 -  **Evaluation metrix**
 -  **Monitoring System**

# Installation
1️⃣ Clone the Repository

**git clone https://github.com/<your-username>/PDF_CHAT_AI.git
cd PDF_CHAT_AI**


2️⃣ Create and Activate a Virtual Environment (Recommended)

python -m venv venv

- macOS / Linux
**source venv/bin/activate**

- Windows
**venv\Scripts\activate**

3️⃣ Install Dependencies

 - **pip install -r requirements.txt**


Your requirements.txt should include:

 - **pypdf**
 - **ollama**
 - **numpy**
 - **sentence-transformers**

4️⃣ Install and Configure Ollama

Download Ollama from:

https://ollama.com

Pull the LLaMA3 model:

 - **ollama pull llama3**

▶️ Usage

Run the application:

 - **python pdf_chat.py**


You will be prompted to enter the path to a PDF file:

 - **Enter the path to your PDF file:**


After loading:

 - The document is chunked

 - Embeddings are generated

 - You can start asking questions

Type exit to quit.

# Example Questions

 - "What is the main objective of this document?"

 - "Explain the concept of neural networks mentioned in the PDF."

 - "What does the document say about data preprocessing?"

 - "Summarize the key points discussed in Chapter 2."

Because this version uses semantic search, it can handle:

 - Synonyms

 - Paraphrased questions

 - Conceptual queries

 - Non-exact word matches

# Known Limitations

 - Embeddings are generated at runtime (not persisted)

 - No FAISS or scalable vector database yet

 - Large PDFs may increase initial loading time

 - CLI-based (no web interface yet)

These limitations motivate future upgrades.


 # Planned Improvements

Future versions will include:

Persistent embedding storage

 - FAISS-based scalable vector search

 - Page-number citations in answers

 - Modular architecture (separate ingestion/retrieval modules)

 - Optional FastAPI or Streamlit interface

 - Streaming LLM responses

# Learning Outcomes

By building this version, you gain hands-on understanding of:

 - Core RAG architecture

 - Sentence-based chunking strategies

 - Embedding models and vector representations

 - Cosine similarity mechanics

 - Retrieval grounding techniques

 - How production RAG systems are structured internally
# License

This project is intended for educational purposes.

# 👤 Author

Saikat Gayen
Aspiring AI / LLM Engineer
Python | RAG Systems | Local LLMs | Retrieval Engineering

