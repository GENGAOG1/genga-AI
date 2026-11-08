import os
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_ai(prompt: str) -> str:
    key = os.getenv("OPENROUTER_API_KEY")
    model = os.getenv("OPENROUTER_MODEL")
    if not key or not model:
        return "OpenRouter ist noch nicht konfiguriert. Bitte API-Key und Modell in den Umgebungsvariablen setzen."
    response = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"model": model, "messages": [{"role": "user", "content": prompt}]},
        timeout=90,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
