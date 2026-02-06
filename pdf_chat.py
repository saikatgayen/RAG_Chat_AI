from pypdf import PdfReader # type: ignore
from ollama import chat # type: ignore
import os

#------------ Extract Text from PDF ------------

def Extract_Text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

        return text
    
#------------ Ask LLM with content ------------


def ask_pdf(pdf_text, question):
    prompt = f"""
    Answer strictly using the PDF content.
 If the answer cannot be confidently inferred, say "Not found in the document."


PDF Content:
{pdf_text}

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

    print("PDF loaded successfully. You can now ask questions about its content.")
    print("Ask your questions below (type 'exit' to quit):\n")

    while True:
        question = input(">> ")


        if question.lower() == 'exit':
            break

        answer = ask_pdf(pdf_text, question)
        print("\n", answer, "\n")
