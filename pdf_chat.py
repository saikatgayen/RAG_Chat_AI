from ollama import chat
from rag_utils import extract_pdf_text, chunk_text, retrieve_chunks, build_prompt


PDF_PATH = "ML3.pdf"

def main():
    print("LOADING PDF...")
    text = extract_pdf_text(PDF_PATH)

    print("CHUNKING TEXT...")
    chunks = chunk_text(text)

    print("PDF ready. Ask questions (type 'exit' to quit)\n")

    while True:
        question = input("QUESTION:")
        if question.lower() == "exit":
            break


        relevant_chunks = retrieve_chunks(question, chunks)
        prompt = build_prompt(relevant_chunks, question)

      
        response = chat(
            model = "llama3",
            messages = [{"role":"user", "container": prompt}]
        )


        print("\n ANSWER:")
        print(response["message"]["content"])
        print("-" * 50)


if __name__ == "__main__":
     main()
