from pypdf import PdfReader 
from ollama import chat
from sentence_transformers import SentenceTransformer
import numpy as np
import os
import re
import faiss
import pickle


INDEX_PATH = "vector_store/index.faiss"
META_PATH = "vector_store/metadata.pkl"

#------------ Load  embedding model ------------

print("Loading embedding model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

#------------ Extract Text from PDF with Page Numbers ------------

def Extract_Text(pdf_path):
    reader = PdfReader(pdf_path)
    chunks = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            sentences = re.split(r'(?<=[.!?])\s+', text)

            current_chunk = ""
            for sentence in sentences:
                if len(current_chunk) + len(sentence) <= 900:
                    current_chunk += " " + sentence
                else:
                    chunks.append({
                        "text": current_chunk.strip(),
                        "page": page_number + 1
                    })
                    current_chunk = sentence

            if current_chunk:
                chunks.append({
                    "text": current_chunk.strip(),
                    "page": page_number + 1
                })        

    return chunks        

    
#------------ Build FAISS Index ------------

def build_vector_store(chunks):
    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedding_model.encode(texts, normalize_embeddings=True)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    os.makedirs("vector_store", exist_ok = True)
    faiss.write_index(index, INDEX_PATH)

    with open(META_PATH, "wb") as f:
        pickle.dump(chunks, f)

    return index, chunks    

#------------ Load Existing Index ------------

def load_vector_store():
    index = faiss.read_index(INDEX_PATH)
    
    with open(META_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks

#------------ Retrieval of relevant chunks ------------

def retrieve(index, chunks, question, top_k=5):
    question_embedding = embedding_model.encode([question], normalize_embeddings=True)
    distances, indices = index.search(np.array(question_embedding), top_k)

    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return results    

#------------ Ask LLM ------------

def ask_pdf(chunks, index, question):
    retrieved = retrieve(index, chunks, question)

    context = ""
    for chunk in retrieved:
        context += f"Page {chunk['page']}:\n{chunk['text']}\n\n"

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


    if not os.path.exists(INDEX_PATH):
        print("Building vector store...")
        chunks = Extract_Text(pdf_path)
        index, chunks = build_vector_store(chunks)
        print("Index built and saved.")
    else:
        print("Loading existing vector store...")
        index, chunks = load_vector_store()

    print("Ask your questions below (type 'exit' to quit):\n")


    while True:
        question = input(">> ")


        if question.lower() == 'exit':
            break

        answer = ask_pdf(chunks, index, question)
        print("\n", answer, "\n")
