
from fastapi import FastAPI

app = FastAPI(
    title="Japan Travel RAG API",
    description="RAG API for Japan travel recommendations",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "RAG API is running"
    }