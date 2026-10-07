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

        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv(
            "OPENAI_MODEL",
            "gpt-4o-mini"
        )

        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.anthropic_model = os.getenv(
            "ANTHROPIC_MODEL",
            "claude-3-5-haiku-latest"
        )

    def generate(self, message, history=None, provider="ollama"):
        history = history or []

        if provider == "openai":
            return self._openai(message, history)

        if provider == "claude":
            return self._claude(message, history)

        return self._ollama(message, history)

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

    def _openai(self, message, history):
        if not self.openai_api_key:
            return {
                "provider": "openai",
                "response": "OpenAI API key is not configured."
            }

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

        headers = {
            "Authorization": f"Bearer {self.openai_api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.openai_model,
            "messages": messages
        }

        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            return {
                "provider": f"openai/{self.openai_model}",
                "response": data["choices"][0]["message"]["content"]
            }

        except requests.exceptions.RequestException as exc:
            return {
                "provider": "openai",
                "response": f"OpenAI is unavailable: {exc}"
            }

    def _claude(self, message, history):
        if not self.anthropic_api_key:
            return {
                "provider": "claude",
                "response": "Claude API key is not configured."
            }

        messages = []

        for item in history:
            if item["role"] in ["user", "assistant"]:
                messages.append({
                    "role": item["role"],
                    "content": item["content"]
                })

        messages.append({
            "role": "user",
            "content": message
        })

        headers = {
            "x-api-key": self.anthropic_api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.anthropic_model,
            "max_tokens": 512,
            "messages": messages
        }

        try:
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            return {
                "provider": f"claude/{self.anthropic_model}",
                "response": data["content"][0]["text"]
            }

        except requests.exceptions.RequestException as exc:
            return {
                "provider": "claude",
                "response": f"Claude is unavailable: {exc}"
            }
