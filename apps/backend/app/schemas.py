from typing import Literal

from pydantic import BaseModel


class StatsResponse(BaseModel):
    stats: dict[str, float] 

class Decision(BaseModel):
    title: str
    type: Literal["scales", "binary"]
    description: str


class StatChange(BaseModel):
    choices: float
    production: float
    total: float
    end: float


class TurnSummary(BaseModel):
    turn: int
    stats: dict[str, StatChange]


class ChoiceResult(BaseModel):
    alive: bool
    stats: dict[str, float]
    summary: TurnSummary | None = None

class Turn(BaseModel):
    turn: int
