from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthCheck(BaseModel):
    status: str = "ok"


@router.get("/health", response_model=HealthCheck)
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok"}
