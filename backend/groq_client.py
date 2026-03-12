import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_issue(issue_text: str):

    prompt = f"""
You are a senior software engineer.

Analyze this GitHub issue:

{issue_text}

Return STRICT JSON like:

{{
  "explanation": "...",
  "checklist": ["...", "..."],
  "priority": "low | medium | high",
  "label": "bug | enhancement | documentation"
}}
"""

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )

    return chat.choices[0].message.content 