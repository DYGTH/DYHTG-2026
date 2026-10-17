from pydantic import BaseModel


class StatsResponse(BaseModel):
    stats: dict[str, float] 

class Event(BaseModel):
    id: str
    title: str
    description: str


class EventsResponse(BaseModel):
    events: list[Event]


class Decision(BaseModel):
    id: str
    event_id: str  
    description: str


class DecisionsResponse(BaseModel):
    decisions: list[Decision]


class ChoiceRequest(BaseModel):
    choices: list[str] 


class TurnResult(BaseModel):
    turn: int
    alive: bool
    stats: dict[str, float]
