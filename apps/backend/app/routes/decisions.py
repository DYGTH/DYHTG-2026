from fastapi import APIRouter, HTTPException

from app.schemas import ChoiceRequest, DecisionsResponse, TurnResult
from app.services import game_service

router = APIRouter(tags=["decisions"])


@router.get("/events/{event_id}/decisions", response_model=DecisionsResponse)
def list_decisions(event_id: str):
    decisions = game_service.get_decisions(event_id)
    if decisions is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return DecisionsResponse(decisions=decisions)


@router.post("/choices", response_model=TurnResult)
def submit_choices(body: ChoiceRequest):
    return game_service.submit_choices(body.choices)
