from fastapi import APIRouter

from app.routes import decisions, events, health, stats, turn

router = APIRouter()
router.include_router(health.router)
router.include_router(stats.router)
router.include_router(events.router)
router.include_router(decisions.router)
router.include_router(turn.router)
