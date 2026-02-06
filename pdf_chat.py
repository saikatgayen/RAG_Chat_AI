
from pypdf import PdfReader # type: ignore
from ollama import chat # type: ignore


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
    You are answering strictly from the given PDF content.
If the answer is not in the PDF, say Not found in the document."



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
    pdf_path = "ML3.pdf"  # Path to your PDF file
    pdf_text = Extract_Text(pdf_path)

    print("PDF loaded. Ask questions (type 'exit' to quit)\n")

    while True:
        question = input(">> ")


        if question.lower() == 'exit':
            break

        answer = ask_pdf(pdf_text, question)
        print("\n", answer, "\n")
