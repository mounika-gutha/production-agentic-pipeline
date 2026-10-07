# 🤖 Production Agentic Pipeline & Orchestration Engine

> A simple agentic AI pipeline that connects **n8n, Flask, MongoDB, Ollama, Docker, and GitHub Actions** to process user requests, generate AI responses using a local LLM, and automate testing and Docker image publishing.

## 🌟 Highlights

- 🤖 Local AI using **Ollama + Qwen 2.5 0.5B**
- 🔄 Workflow automation using **n8n**
- 🧠 Conversation memory using **MongoDB**
- 🚀 REST API built with **Flask**
- 🛠️ External tool integration
- 🐳 Docker containerization
- 🧪 Automated testing using **pytest**
- ⚙️ GitHub Actions CI/CD
- 📦 Docker image publishing using **GitHub Container Registry (GHCR)**
- 💰 Free local LLM setup with no paid API required

## 🏗️ System Architecture

![System Architecture](docs/architecture.png)

## ℹ️ Overview

This project demonstrates a simple **agentic AI workflow** where user requests are processed through an n8n workflow and Flask backend.

MongoDB stores conversation history, while Ollama runs the **Qwen 2.5 0.5B** model locally to generate AI responses.

The project also includes a **GitHub Actions CI/CD pipeline** that automatically runs tests, builds the Docker image, and publishes the image to GitHub Container Registry when changes are pushed to the `main` branch.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| Flask | REST API |
| n8n | Workflow orchestration |
| MongoDB | Conversation memory |
| Ollama | Local LLM |
| Qwen 2.5 0.5B | AI model |
| Docker | Containerization |
| Docker Compose | Service management |
| pytest | Automated testing |
| GitHub Actions | CI/CD |
| GitHub Container Registry | Docker image registry |
| HTML/CSS/JavaScript | Frontend |
| Git/GitHub | Version control |

## 🚀 How It Works

~~~text
User
  ↓
Frontend / n8n
  ↓
Flask Backend
  ↓
MongoDB ← Conversation Memory
  ↓
Ollama
  ↓
Qwen 2.5 0.5B
  ↓
AI Response
~~~

1. User sends a message through the frontend or n8n.
2. Flask receives the request.
3. Previous messages are retrieved from MongoDB.
4. Flask sends the request to Ollama.
5. Qwen 2.5 0.5B generates the response.
6. The conversation is stored in MongoDB.
7. The response is returned to the user.

## ⚙️ CI/CD Pipeline

~~~text
Developer
  ↓
Git Push
  ↓
GitHub Repository
  ↓
GitHub Actions
  ↓
Install Dependencies
  ↓
Run pytest
  ↓
Build Docker Image
  ↓
Push Image to GHCR
~~~

The Docker image is published as:

~~~text
ghcr.io/mounika-gutha/production-agentic-pipeline:latest
~~~

## 📁 Project Structure

~~~text
production-agentic-pipeline/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── models/
│   └── services/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── n8n/
│   └── workflows/
│       └── agentic-pipeline.json
│
├── tests/
│   ├── __init__.py
│   └── test_backend.py
│
├── docs/
│   ├── architecture.png
│   ├── architecture.md
│   └── workflow.md
│
├── Dockerfile
├── .env.example
├── docker-compose.yml
└── README.md
~~~

## ⬇️ Installation

### 1. Clone the repository

~~~bash
git clone git@github.com:mounika-gutha/production-agentic-pipeline.git
cd production-agentic-pipeline
~~~

### 2. Create virtual environment

~~~bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
~~~

### 3. Start MongoDB and n8n

~~~bash
docker compose up -d
~~~

### 4. Start Ollama

~~~bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
~~~

### 5. Start Flask

~~~bash
python backend/app.py
~~~

Backend:

`http://localhost:5000`

n8n:

`http://localhost:5678`

Ollama:

`http://localhost:11434`

## 🌐 Frontend

~~~bash
cd frontend
python3 -m http.server 5500
~~~

Frontend:

`http://localhost:5500`

## 💬 Example

~~~bash
curl -X POST http://localhost:5000/api/chat \
-H "Content-Type: application/json" \
-d '{"message":"Explain DevOps in simple words","session_id":"demo-session","provider":"ollama"}'
~~~

The request flows through:

~~~text
Flask → Ollama → Qwen 2.5 0.5B → Response
~~~

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application status |
| GET | `/health` | Health check |
| POST | `/api/chat` | Send message |
| GET | `/api/sessions/<id>/messages` | Get conversation history |
| GET | `/api/tools/demo` | Test external tool |

## 🐳 Docker

Build the Docker image:

~~~bash
docker build -t production-agentic-pipeline:test .
~~~

The Docker image contains the Flask backend and its Python dependencies.

## 🧪 Testing

Run tests locally:

~~~bash
pytest
~~~

GitHub Actions automatically runs the tests during the CI/CD pipeline.

## 📦 GitHub Container Registry

GitHub Actions builds and publishes the Docker image to **GHCR**:

~~~text
GitHub
  ↓
GitHub Actions
  ↓
Docker Build
  ↓
GitHub Container Registry
~~~

Docker image:

~~~text
ghcr.io/mounika-gutha/production-agentic-pipeline:latest
~~~

## 🎯 What I Learned

- AI and LLM integration
- Local LLM deployment using Ollama
- REST API development with Flask
- Workflow automation with n8n
- MongoDB conversation memory
- Docker containerization
- Docker Compose
- Automated testing with pytest
- Git and GitHub
- GitHub Actions CI/CD
- Docker image publishing using GHCR

## 👩‍💻 Author

**Gutha Mounika**

B.Tech CSE – Artificial Intelligence & Machine Learning

[GitHub](https://github.com/mounika-gutha)


## ⭐ Project

If you find this project useful, feel free to explore the repository and give it a ⭐.