from fastapi import APIRouter

from app.schemas import EventsResponse
from app.services import game_service

router = APIRouter(tags=["events"])


@router.get("/events", response_model=EventsResponse)
def list_events():
    return EventsResponse(events=game_service.get_events())
