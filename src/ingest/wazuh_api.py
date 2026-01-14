from fastapi import APIRouter
from src.ingest.schemas.wazuh import WazuhEvent

router = APIRouter()

@router.post("/")
def ingest_wazuh(event: WazuhEvent):
    return {"status": "ok"}