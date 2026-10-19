import sys
import threading
from pathlib import Path

from app.schemas import ChoiceResult, Decision, Turn

root = Path(__file__).resolve().parents[4]
src = root / "apps" / "src"
sys.path[:0] = [str(root), str(src), str(src / "shared_types")]

import exposure  # noqa: E402
import game  # noqa: E402


def start_game():
    threading.Thread(target=game.start_game, daemon=True).start()


def get_stats() -> dict[str, float]:
    return exposure.get_stats_for_frontend()


def get_turn() -> Turn:
    return Turn(turn=exposure.get_turn_for_frontend())


def get_decision() -> Decision | None:
    decision = exposure.get_decision_for_frontend()
    return Decision(**decision) if decision else None


def submit_choice(data: dict) -> ChoiceResult:
    turn = exposure.get_turn_for_frontend()
    exposure.receive_choice_from_frontend(data)
    summary = exposure.get_turn_summary_for_frontend()
    if summary is not None and summary["turn"] != turn:
        summary = None
    return ChoiceResult(alive=exposure.get_alive_for_frontend(), stats=get_stats(), summary=summary)
