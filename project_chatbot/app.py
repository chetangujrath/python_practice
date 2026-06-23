from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "answer": ""
        }
    )

@app.post("/", response_class=HTMLResponse)
async def ask(
    request: Request,
    question: str = Form(...)
):

    prompt = f"""
    Act as Senior DevOps Interviewer.

    Question:
    {question}

    Give:
    1. Answer
    2. Explanation
    3. Real-world scenario
    """

    response = model.generate_content(
        prompt
    )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "answer": response.text
        }
    )