from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bharat Api is Live"}

@app.get("/ask")
def ask(q: str):
    return {"question": q, "answer": "Jai Hind! Ye aapka jawab hai - " + q}
