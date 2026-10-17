# COMMUNICATE WITH MIDDLEMAN

from shared_types import Choice, World, Civilisation

DECISION_TYPES = ("scales", "binary")

decision = None
choice = None

def pass_decision_to_frontend(data: dict):
    global decision
    data = {str(key).lower(): value for key, value in data.items()}
    if data["type"] not in DECISION_TYPES:
        raise ValueError(f"decision type must be one of {DECISION_TYPES}, got {data['type']!r}")
    decision = data

def get_decision_for_frontend():
    if decision is None:
        return None
    return {key: decision[key] for key in ("title", "type", "description")}

def receive_choice_from_frontend(data: dict):
    global decision, choice
    if decision is None:
        raise LookupError("No pending decision")

    answer = data.get("answer")
    if decision["type"] == "binary":
        answer = str(answer).lower()
        if answer not in ("yes", "no"):
            raise ValueError("binary decision needs yes or no")
        value = answer == "yes"
    else:
        try:
            value = float(answer)
        except (TypeError, ValueError):
            raise ValueError("scales decision needs a number")

    choice = Choice(decision)
    choice.value = value
    decision = None

def pass_civ_world_to_frontend(civ: Civilisation, world: World):

    pass