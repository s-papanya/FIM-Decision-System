from fastapi import FastAPI
from src.ingest.api import router as ingest_router

app = FastAPI(title="FIM Decision System")

app.include_router(ingest_router, prefix="/ingest")

@app.get("/health")
def health():
    return {"status": "ok"}
