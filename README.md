# 🤖 AI GitHub Issue Agent (MCP + n8n + Groq)

An autonomous AI agent that analyzes GitHub issues and automatically posts debugging checklists and recommendations using LLM reasoning.

## 🚀 Features

* AI issue analysis using Groq LLM
* MCP tool architecture for agent actions
* n8n workflow automation
* Automatic GitHub comments
* Issue labeling support
* Event-driven DevOps workflow

## 🧠 Architecture

GitHub Issue → n8n Webhook → Backend Agent → Groq LLM → MCP Tool → GitHub Comment

## 🛠 Tech Stack

* FastAPI
* Groq LLM
* n8n
* MCP (Model Context Protocol)
* GitHub API

## ▶️ Run locally

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## 🔐 Environment

Create `.env` from `.env.example`.

## 📌 Use Case

Acts as an AI developer assistant that helps triage issues, generate debugging steps, and automate DevOps workflows.

## ⭐ Future Work

* PR generation
* Multi-agent orchestration
* Repo knowledge RAG
* CI failure analysiss
