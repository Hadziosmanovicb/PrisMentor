
from fastapi import FastAPI

app = FastAPI(title="PrisMentor API")

@app.get("/")
def home():
    return {"message": "PrisMentor virker!"}

@app.get("/health")
def health():
    return {"status": "ok"}
