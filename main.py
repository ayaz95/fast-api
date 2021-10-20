from fastapi import FastAPI
import uvicorn
from core.config import settings

app = FastAPI(title='jobboard', version='0.0.1')

@app.get("/")
def home():
    return {"Details":"Test"}
