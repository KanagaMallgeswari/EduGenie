from fastapi import FastAPI,Request,Form
from google import genai
import os
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")
@app.get("/")
def home():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())
@app.post("/")
def submit(task: str=Form(...), text: str=Form(...)):
    if task == "qa":
        result = answer_question(text)
    elif task == "explain":
        result = explain_topic(text)
    elif task  == "quiz":
        result = generate_quiz(text)
    elif task == "summarize":
        result = summarize_text(text)
    elif task == "learn":
        result = recommend_learning_path(text)
    else:
        result = "Invalid task"
    return {"result":result}
@app.post("/qa")
def qa(question:str):
    return{"answer":answer_question(question)}
@app.post("/explain")
def explain(topic:str):
    return{"explanation":explain_topic(topic)}
@app.post("/quiz")
def quiz(topic:str):
    return{"quiz":generate_quiz(topic)}
@app.post("/summarize")
def summarize(text:str):
    return{"summarize":summarize_text(text)}
@app.post("/learn/recommendations")
def learning_path(topic:str):
    return{"recommendation":recommendation_learning_path(topic)}