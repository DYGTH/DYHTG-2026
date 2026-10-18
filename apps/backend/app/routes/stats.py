from fastapi import APIRouter

from app.schemas import StatsResponse
from app.services import game_service

router = APIRouter(tags=["stats"])


@router.get("/stats", response_model=StatsResponse)
def list_stats():
    return StatsResponse(stats=game_service.get_stats())
