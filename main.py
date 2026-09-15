from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Bharat-Api")

MY_SECRET_KEY = "BHARAT-10000-KEY"

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Bharat API Live Hai", "version": "1.0"}

@app.post("/api/chat")
def chat(req: ChatRequest, x_api_key: str = Header(None)):
    if x_api_key != MY_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Galat API Key")
    return {"reply": f"Bharat-Api ka Jawab: Aapne bola {req.message}"}
