from pypdf import PdfReader 
from ollama import chat
from sentence_transformers import SentenceTransformer
import numpy as np
import os
import re

#------------ Load  embedding model ------------

print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniL-L6-v2")

#------------ Extract Text from PDF ------------

def Extract_Text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text
    

#------------ Chunk Text ------------

def chunk_text(text, chunk_size=500, overlap=100):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip()) #overlap handled by keeping last parts of the chunk
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

#------------ Retrieval of relevant chunks ------------

def retrieve_chunks(chunks, question, top_k=9):
    question_words = set(re.findall(r"\w+", question.lower()))
    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(re.findall(r"\w+", chunk.lower()))
        score = len(question_words.intersection(chunk_words))
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key= lambda x: x[0], reverse= True)

    return [chunk for score, chunk in scored_chunks[:top_k]]


#------------ Ask LLM with context ------------

def ask_pdf(chunks, question):
    relevant_chunks = retrieve_chunks(chunks, question)

    if chunks[0] not in relevant_chunks:
        relevant_chunks.insert(0, chunks[0])

    if not relevant_chunks:
        relevant_chunks = chunks[:2] # Fallback to the first few chunks if no relevance found
    
    context = "\n\n".join(relevant_chunks)

    prompt = f"""
Answer using the PDF content. If the answer is clearly not present,
say "Not found in the document."



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

    print("Ask your questions below (type 'exit' to quit):\n")


    while True:
        question = input(">> ")


        if question.lower() == 'exit':
            break

        answer = ask_pdf(chunks, question)
        print("\n", answer, "\n")
