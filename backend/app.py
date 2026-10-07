import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

from backend.services.memory import MemoryStore
from backend.services.llm_router import LLMRouter
from backend.services.tools import get_demo_tool_result

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__)
CORS(app)

memory = MemoryStore(
    os.getenv("MONGO_URI", "mongodb://localhost:27017"),
    os.getenv("MONGO_DB", "agentic_pipeline")
)

router = LLMRouter()


@app.get("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/style.css")
def style():
    return send_from_directory(FRONTEND_DIR, "style.css")


@app.get("/script.js")
def script():
    return send_from_directory(FRONTEND_DIR, "script.js")


@app.get("/health")
def health():
    ok = memory.health()

    return jsonify(
        status="healthy" if ok else "degraded",
        mongodb="connected" if ok else "unavailable"
    ), (200 if ok else 503)


@app.post("/api/chat")
def chat():
    d = request.get_json(silent=True) or {}

    msg = str(d.get("message", "")).strip()
    sid = str(d.get("session_id", "default")).strip() or "default"
    provider = str(d.get("provider", "ollama")).lower()

    if not msg:
        return jsonify(error="message is required"), 400

    history = memory.get_messages(sid)

    result = router.generate(
        msg,
        history,
        provider
    )

    memory.add_message(
        sid,
        "user",
        msg
    )

    memory.add_message(
        sid,
        "assistant",
        result["response"]
    )

    return jsonify(
        session_id=sid,
        provider=result["provider"],
        response=result["response"],
        memory_messages=len(history) + 2
    )


@app.get("/api/sessions/<sid>/messages")
def messages(sid):
    return jsonify(
        session_id=sid,
        messages=memory.get_messages(sid)
    )


@app.get("/api/tools/demo")
def tool():
    return jsonify(get_demo_tool_result())


if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(
        os.getenv(
            "PORT",
            os.getenv("FLASK_PORT", "5000")
        )
    )

    app.run(
        host=host,
        port=port
    )
