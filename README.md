# PDF_CHAT_AI (Basic RAG – Local LLM)

A **basic Retrieval-Augmented Generation (RAG) proof-of-concept** project that allows users to chat with a PDF document using a **locally hosted LLM (Ollama + LLaMA3)**.

This project is intentionally kept **simple and minimal** to clearly demonstrate the *core idea of RAG*: grounding a language model’s responses in external documents (PDFs), before introducing advanced techniques like embeddings, vector databases, or APIs.

---

##  Project Overview

The application:

* Loads a PDF file
* Extracts all textual content
* Uses the extracted text as **context**
* Passes the context + user question to a local LLM
* Returns answers **strictly based on the PDF content**

If the answer does not exist in the document, the model is instructed to say so.

This version represents **RAG v0 (Naive RAG)**.

---

##  Why This Project

This project was built as a **learning-first RAG implementation**, focusing on:

* Understanding how document grounding works
* Seeing the limitations of naive context injection
* Building intuition for why chunking, retrieval, and embeddings are necessary

Rather than starting with complex architectures, this project builds a strong conceptual foundation.

---

##  Project Structure

```
pdf_chat_basic/
├── pdf_chat.py          # Main CLI application
├── data/
│   └── sample.pdf       # PDF document to query
├── requirements.txt     # Project dependencies
└── README.md
```

---

##  Tech Stack

* **Python**
* **Ollama** (Local LLM runtime)
* **LLaMA3** (Language Model)
* **PyPDF** (PDF text extraction)

No cloud APIs or external services are used.

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/PDF_CHAT_AI.git
cd PDF_CHAT_AI
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

* Install Ollama from: [https://ollama.com](https://ollama.com)
* Pull the model:

```bash
ollama pull llama3
```

---

##  Usage

1. Place your PDF file inside the `data/` directory
2. Update the PDF path in `pdf_chat.py` if needed
3. Run the application:

```bash
python pdf_chat.py
```

4. Ask questions in the terminal
5. Type `exit` to quit

---

##  Example Questions

* "What is this document about?"
* "Summarize the main topic."
* "What does the author say about X?"

The model will answer **only if the information exists in the PDF**.

---

##  Known Limitations

This version intentionally has limitations:

* Entire PDF is sent as context (token-heavy)
* Not scalable for large documents
* No chunking or semantic retrieval
* Slower responses for big PDFs

These limitations are **intentional** and motivate the next iterations.

---

##  Future Improvements

Planned upgrades include:

* Text chunking
* Semantic retrieval
* Embeddings with SentenceTransformers
* Vector search using FAISS
* Modular project structure
* FastAPI backend

---

##  Learning Outcomes

Through this project, you will understand:

* What RAG is at a fundamental level
* How LLMs can be grounded in external data
* Why naive approaches fail
* How real-world RAG systems evolve

---

## 👤 Author

**Saikat Gayen**

Aspiring AI / LLM Engineer | Python | RAG Systems | Local LLMs
