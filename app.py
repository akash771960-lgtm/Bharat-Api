from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Bharat Api is Live", "status": "live", "api": "/api/chat"}

@app.get("/ask")
def ask(q: str):
    return {"question": q, "answer": f"🇮🇳 Bharat AI ka jawab: {q}"}

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    sawal = data.get("message", "Hello")
    return {"jawab": f"🇮🇳 Bharat AI: Aapne pucha '{sawal}'", "status": "success"}
