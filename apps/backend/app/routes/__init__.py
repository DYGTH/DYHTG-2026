from fastapi import APIRouter

from app.routes import decisions, events, health, stats

router = APIRouter()
router.include_router(health.router)
router.include_router(stats.router)
router.include_router(events.router)
router.include_router(decisions.router)
