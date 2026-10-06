# Production Agentic Pipeline & Orchestration Engine

Beginner-friendly agentic workflow project using Flask, n8n, MongoDB, and OpenAI/Claude.

## Quick start
```bash
cp .env.example .env
docker compose up -d
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/app.py
```
API: http://localhost:5000  |  n8n: http://localhost:5678

## API
```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/api/chat -H 'Content-Type: application/json' -d '{"session_id":"demo","message":"Explain CI/CD simply","provider":"auto"}'
```
Do not commit `.env` or API keys. This is a portfolio/learning implementation.
