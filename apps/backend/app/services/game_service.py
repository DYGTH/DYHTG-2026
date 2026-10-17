from app.schemas import Decision, Event, TurnResult

# single player: one game for the whole server
_turn = 0
_alive = True


def get_stats() -> dict[str, float]:
    #TO_DO 
    return {"money": 0, "population": 0}


def get_events() -> list[Event]:
    #TO_DO 
    return [Event(id="stub", title="Placeholder event", description="...")]


def get_decisions(event_id: str) -> list[Decision] | None:
    #TO_DO 
    if event_id not in {e.id for e in get_events()}:
        return None
    return [Decision(id="stub", event_id=event_id, description="Placeholder decision")]


def submit_choices(choices: list[str]) -> TurnResult:
    #TO_DO 
    global _turn
    _turn += 1
    return TurnResult(turn=_turn, alive=_alive, stats=get_stats())
