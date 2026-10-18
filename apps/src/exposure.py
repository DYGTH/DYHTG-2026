""" COMMUNICATE WITH MIDDLEMAN """

from shared_types import Choice, Decision, World, Civilisation

DECISION_TYPES = ("scalar", "binary")

decision = None
choice = None
stats = {}
alive = True

def pass_decision_to_frontend(new_decision: Decision):
    global decision
    if new_decision.type not in DECISION_TYPES:
        raise ValueError(f"decision type must be one of {DECISION_TYPES}, got {new_decision.type!r}")
    decision = new_decision

def get_decision_for_frontend():
    if decision is None:
        return None
    return {"title": decision.title, "type": decision.type, "description": decision.description}

def receive_choice_from_frontend(data: dict):
    global decision, choice
    if decision is None:
        raise LookupError("No pending decision")

    choise_answer = data.get("choise_answer")
    if decision.type == "binary":
        if not isinstance(choise_answer, bool):
            raise ValueError("binary decision needs true or false")
        value = choise_answer
    else:
        try:
            value = float(choise_answer)
        except (TypeError, ValueError):
            raise ValueError("scales decision needs a number")

    choice = Choice(decision, value)
    decision = None

def get_choice_from_frontend():
    global choice
    answer, choice = choice, None
    return answer

def pass_civ_world_to_frontend(civ: Civilisation, world: World):
    global stats, alive
    stats = {**civ.get_stat(), **world.get_stat()}
    alive = civ.isAlive() 

def get_stats_for_frontend():
    return stats

def get_alive_for_frontend():
    return alive