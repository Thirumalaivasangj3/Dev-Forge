import requests
from groq_client import analyze_issue

MCP_URL = "http://localhost:8001/tool/create_checklist"

def handle_issue(issue_text: str):

    # AI reasoning
    analysis = analyze_issue(issue_text)

    # Call MCP tool
    try:
        requests.post(MCP_URL, json={"analysis": analysis}, timeout=10)
    except Exception as e:
        print("MCP call failed:", e)

    return analysis 