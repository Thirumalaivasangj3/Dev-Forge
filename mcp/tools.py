import os
import requests
from dotenv import load_dotenv

load_dotenv()

def create_checklist(analysis: str):

    webhook = os.getenv("N8N_WEBHOOK")

    requests.post(
        webhook,
        json={"analysis": analysis}
    ) 