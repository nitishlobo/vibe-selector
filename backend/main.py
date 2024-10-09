"""Main app."""

from fastapi import APIRouter, FastAPI
from settings import APP_TITLE, DEBUG_BACKEND_V1
from v1.views.health_check import router as health_check_router

# Main app and versions
main_app = FastAPI(title=APP_TITLE, version="1.0.0", debug=DEBUG_BACKEND_V1)

v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(health_check_router)
