from fastapi import APIRouter
from src.ingest.wazuh_api import router as wazuh_router

router = APIRouter()

router.include_router(wazuh_router, prefix="/wazuh")