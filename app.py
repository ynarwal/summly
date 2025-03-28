from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import pdfplumber
import json
import os
from dotenv import load_dotenv
from docx import Document

load_dotenv()

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI Client Setup
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OpenAI API Key in environment variables")
openai_client = OpenAI(api_key=openai_api_key)


def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(
            [page.extract_text() for page in pdf.pages if page.extract_text()]
        )


def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])



@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    text = ""
    if file.content_type == "application/pdf" or file.file.name.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    elif file.content_type in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword",
    ] or file.file.name.endswith(".docx"):
        text = extract_text_from_docx(file.file)
    if not text:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant that summarizes documents. Your task is to summarize the given document in four formats.",
            },
            {
                "role": "user",
                "content": f"""
                Summarize the following text into key points and return a structured JSON response.

                Provide four distinct summaries:

                1. **Short Version** (30-50 words)
                2. **Detailed Version** (100-200 words)
                3. **Technical Version** (if applicable): (Keep domain-specific terms)
                4. **Layman Version** (simplify complex ideas)

                Return the response strictly in this JSON format:
                {{
                    "short_version": "...",
                    "detailed_version": "...",
                    "technical_version": "...",
                    "layman_version": "..."
                }}

                Here is the text to summarize:
                {text}
                """,
            },
        ],
        response_format={"type": "json_object"},
    )
    summary = response.choices[0].message.content.strip()
    return json.loads(summary)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
