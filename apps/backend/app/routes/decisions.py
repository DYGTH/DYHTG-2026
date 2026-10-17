from fastapi import APIRouter, HTTPException

from app.schemas import ChoiceResult, Decision
from app.services import game_service

router = APIRouter(tags=["decision"])


@router.get("/decision", response_model=Decision)
def current_decision():
    decision = game_service.get_decision()
    if decision is None:
        raise HTTPException(status_code=404, detail="No pending decision")
    return decision


@router.post("/decision", response_model=ChoiceResult)
def answer_decision(body: dict):
    try:
        return game_service.submit_choice(body)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
