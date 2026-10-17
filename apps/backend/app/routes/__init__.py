from fastapi import APIRouter

from app.routes import events, health

router = APIRouter()
router.include_router(health.router)
router.include_router(events.router)
