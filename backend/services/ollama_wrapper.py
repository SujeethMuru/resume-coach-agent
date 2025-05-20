import requests

def query_ollama(prompt: str, model: str = "gemma:2b") -> str:
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "appliccation/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["response"]
    except requests.RequestException as e:
        return f"Error talking to Ollama: {e}"