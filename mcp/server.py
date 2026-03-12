from fastapi import FastAPI
from tools import create_checklist

app = FastAPI()

@app.post("/tool/create_checklist")
def tool(data: dict):
    create_checklist(data["analysis"])
    return {"status": "ok"}