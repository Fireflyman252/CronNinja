from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

class PromptRequest(BaseModel):
    prompt: str
    stream: bool = False  # Optional: set to True if you want streaming response

@app.post("/query")
def query_model(request: PromptRequest):
    payload = {
        "model": MODEL_NAME,
        "prompt": request.prompt,
        "stream": request.stream
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=request.stream)
        response.raise_for_status()

        if request.stream:
            output = ""
            for line in response.iter_lines():
                if line:
                    chunk = line.decode("utf-8")
                    output += chunk + "\n"
            return {"response": output.strip()}
        else:
            data = response.json()
            return {"response": data.get("response", "")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
