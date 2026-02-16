nanofrom pypdf import PdfReader 
from ollama import chat
from sentence_transformers import SentenceTransformer
import numpy as np
import os
import re

#------------ Load  embedding model ------------

print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

#------------ Extract Text from PDF ------------

def Extract_Text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text
    
#------------ Sentence-Aware Chunking ------------

def chunk_text(text, chunk_size=1200, overlap=200):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip()) #overlap handled by keeping last parts of the chunk
            current_chunk = current_chunk[-overlap:] + " " + sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

#------------ Create Embeddings for Chunks ------------

def embed_chunks(chunks):
    embeddings = embedding_model.encode(chunks, normalize_embeddings=True)
    return embeddings


#------------ Semantic Retrieval (RAG v2) ------------

def retrieve_chunks_semantic(chunks, chunk_embeddings, question, top_k=10):
    question_embedding = embedding_model.encode([question], normalize_embeddings=True)[0]

    # Cosine similarity
    similarities = np.dot(chunk_embeddings, question_embedding)

    top_indices = np.argsort(similarities)[-top_k:][::-1]

    return [chunks[i] for i in top_indices]


#------------ Ask LLM with Retrieved Context ------------

def ask_pdf(chunks, chunk_embeddings, question):
    relevant_chunks = retrieve_chunks_semantic(chunks, chunk_embeddings, question)

    if not relevant_chunks:
        relevant_chunks = chunks[:2]

    context = "\n\n".join(relevant_chunks)

    prompt = f"""
You are answering strictly from the given PDF content.,
If the answer is not present, say "Not found in the document."


PDF Content:
{context}

Question:
{question}

Answer:
"""
    response = chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]

#------------ Run CLI ------------


if __name__ == "__main__":
    pdf_path = input("Enter the path to your PDF file: ").strip()


    if not os.path.exists(pdf_path):
        print("File not found. Please check the path and try again.")
        exit(1)

    if not pdf_path.lower().endswith('.pdf'):
        print("The specified file is not a PDF. Please provide a valid PDF file.")
        exit(1)

    print("\nLoading PDF...")
    pdf_text = Extract_Text(pdf_path)

    print("Chunking Documents...")
    chunks = chunk_text(pdf_text)
    print(f"Document split into {len(chunks)} chunks.")

    print("Generating embeddings...")
    chunk_embeddings = embed_chunks(chunks)
    print("Embeddings ready.\n")

    print("Ask your questions below (type 'exit' to quit):\n")


    while True:
        question = input(">> ")


        if question.lower() == 'exit':
            break

        answer = ask_pdf(chunks, chunk_embeddings, question)
        print("\n", answer, "\n")
