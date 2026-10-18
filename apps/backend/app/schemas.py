from typing import Literal

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
    title: str
    type: Literal["scales", "binary"]
    description: str


class ChoiceResult(BaseModel):
    alive: bool
    stats: dict[str, float]

class Turn(BaseModel):
    turn: int
