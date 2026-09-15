from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os, requests

app = FastAPI()

MY_SECRET_KEY = "BHARAT-10000-KEY"
GEMINI_KEY = os.environ.get("GEMINI_API_KEY") # Render se ayegi

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home():
    return """<html><head><title>Bharat AI</title><style>body{font-family:Arial;background:#111;color:#fff;padding:20px}.box{background:#222;padding:20px;border-radius:10px}code{color:#0f0}input,button{padding:12px;width:100%;margin:5px 0;border-radius:8px;border:none}button{background:#0f0;font-weight:bold}</style></head><body><h1>🇮🇳 Bharat AI Pro Live</h1><div class="box"><p>URL: <code>/api/chat</code> | Key: <code>BHARAT-10000-KEY</code></p><input id="m" placeholder="Sawal pucho..."><input id="k" placeholder="API Key"><button onclick="test()">Ask Bharat AI</button><p id="r"></p></div><script>async function test(){let m=document.getElementById('m').value,k=document.getElementById('k').value;let res=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json','x-api-key':k},body:JSON.stringify({message:m})});let d=await res.json();document.getElementById('r').innerText=d.reply;}</script><p><a href='/docs' style='color:#0f0'>Developer Docs</a></p></body></html>"""

@app.post("/api/chat")
def chat(req: ChatRequest, x_api_key: str = Header(None)):
    if x_api_key!= MY_SECRET_KEY:
        raise HTTPException(status_code=401, detail="Galat Key")

    # Agar Gemini Key nahi hai to normal reply
    if not GEMINI_KEY:
        return {"reply": f"[AI Key Missing] Aapne bola: {req.message}. Render me GEMINI_API_KEY daalo."}

    # Asli AI Call
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
        payload = {"contents": [{"parts": [{"text": req.message}]}]}
        r = requests.post(url, json=payload, timeout=15)
        data = r.json()
        ai_reply = data['candidates'][0]['content']['parts'][0]['text']
        return {"reply": ai_reply, "model": "Bharat-AI x Gemini"}
    except Exception as e:
        return {"reply": f"AI Error: {str(e)}", "status": "error"}
