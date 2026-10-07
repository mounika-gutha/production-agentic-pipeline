import os
import requests
from dotenv import load_dotenv

load_dotenv()


class LLMRouter:
    def __init__(self):
        self.ollama_url = os.getenv(
            "OLLAMA_URL",
            "http://localhost:11434/api/chat"
        )
        self.ollama_model = os.getenv(
            "OLLAMA_MODEL",
            "qwen2.5:0.5b"
        )

    def generate(self, message, history=None, provider="ollama"):
        history = history or []

        if provider == "ollama" or provider == "auto":
            return self._ollama(message, history)

        return {
            "provider": "ollama",
            "response": "Only the free local Ollama provider is enabled."
        }

    def _ollama(self, message, history):
        messages = []

        for item in history:
            messages.append({
                "role": item["role"],
                "content": item["content"]
            })

        messages.append({
            "role": "user",
            "content": message
        })

        payload = {
            "model": self.ollama_model,
            "messages": messages,
            "stream": False
        }

        try:
            response = requests.post(
                self.ollama_url,
                json=payload,
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            return {
                "provider": f"ollama/{self.ollama_model}",
                "response": data["message"]["content"]
            }

        except requests.exceptions.RequestException as exc:
            return {
                "provider": "ollama",
                "response": f"Ollama is unavailable: {exc}"
            }
