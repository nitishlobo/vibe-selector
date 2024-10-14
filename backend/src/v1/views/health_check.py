"""Health check endpoints."""

from src.v1.views.base import APIRouter, RouteTags

router = APIRouter(prefix="/health-check", tags=[RouteTags.HEALTH_CHECK])


@router.get("/")
async def health_check() -> dict:
    """Health check endpoint."""ß
    return {"message": "App is healthy."}
