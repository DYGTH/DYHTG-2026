from fastapi import APIRouter

from app.schemas import Turn
from app.services import game_service

router = APIRouter(tags=["turn"])


@router.get("/turn", response_model=Turn)
def current_turn():
    return game_service.get_turn()
