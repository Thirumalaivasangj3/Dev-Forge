# AI GitHub Issue Agent (MCP + n8n + Groq)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_LLM-F55036?style=for-the-badge&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub_API-181717?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

> An autonomous AI agent that analyzes GitHub issues and automatically posts debugging checklists and recommendations using LLM reasoning.

---

## Features

| Feature |
|---|
| AI issue analysis using Groq LLM |
| MCP tool architecture for agent actions |
| n8n workflow automation |
| Automatic GitHub comments |
| Issue labeling support |
| Event-driven DevOps workflow |

---

## Architecture

```
GitHub Issue → n8n Webhook → Backend Agent → Groq LLM → MCP Tool → GitHub Comment
```

---

## Tech Stack

| Technology |
|---|
| FastAPI |
| Groq LLM |
| n8n |
| MCP (Model Context Protocol) |
| GitHub API |

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

---

## Environment

Create `.env` from `.env.example`.

---

## Use Case

> Acts as an AI developer assistant that helps triage issues, generate debugging steps, and automate DevOps workflows.

---

## License

MIT License
