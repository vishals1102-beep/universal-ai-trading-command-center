

from fastapi import FastAPI

app = FastAPI(
    title="Universal AI Trading Command Center",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Trading Command Center is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "trading": "manual approval required",
        "auto_execution": False
    }
  
