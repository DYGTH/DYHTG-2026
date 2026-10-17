import sys
from pathlib import Path

from app.schemas import ChoiceResult, Decision, Event

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))

import exposure  # noqa: E402


def get_stats() -> dict[str, float]:
    return exposure.get_stats_for_frontend()


# def get_events() -> list[Event]:
#     #TO_DO
#     return [Event(id="stub", title="Placeholder event", description="...")]


def get_decision() -> Decision | None:
    decision = exposure.get_decision_for_frontend()
    return Decision(**decision) if decision else None


def submit_choice(data: dict) -> ChoiceResult:
    exposure.receive_choice_from_frontend(data)
    return ChoiceResult(alive=exposure.get_alive_for_frontend(), stats=get_stats())
