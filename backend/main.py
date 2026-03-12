from fastapi import FastAPI
from agent import handle_issue

app = FastAPI()

@app.post("/analyze")
def analyze(data: dict):
    result = handle_issue(data["issue"])
    return {"result": result} 