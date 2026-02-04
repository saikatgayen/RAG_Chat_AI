from pypdf import PdfReader


#-----------Text Extraction--------------


def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
         extracted = page.extract_text()
         if extracted:
              text += extracted + "\n"


    return text

#-------------Chunking--------------------


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
         end = start + chunk_size
         chunk = text[start:end]
         chunks.append(chunk)
         start = end - overlap


    return chunks


#------------Naive Retrieval---------------


def retrieve_chunks(question, chunks, top_k=3):
    question_words = set(question.lower().split())
    scored_chunks = []


    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(question_words & chunk_words)
        scored_chunks.append((score, chunk))

   
    scored_chunks.sort(key=lambda x: x[0], reverse = True)
    return [chunk for score, chunk in scored_chunks[:top_k]]


#-----------Prompt taking---------------


def build_prompt(context_chunks, question):
    context = "\n\n".join(context_chunks)


    prompt = f"""

You are a helpful study and research assistant.
Use ONLY the information provided in the context.
If the answer is not present, say you don't know.

Context:
{context}

Question:
{question}

Answer:

"""
    
    return prompt
