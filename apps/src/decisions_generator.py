from apps.src.shared_types import Civilisation, Decision, World

import random

import event_catalogue
from effects import affordable_notches

ICONS = {
    "money": "💰", "food": "🌾", "wood": "🪵", "stone": "🪨", "population": "👥",
    "happiness": "😊", "factories": "🏭", "farms": "🚜", "sawmills": "🪚",
    "quarries": "⛏️", "depollutinators": "🌬️", "available_land": "🏞️",
    "pollution": "☁️", "wild_land": "🌲",
}

SCALE_BY = {
    "money": "factories", "food": "farms", "wood": "sawmills", "stone": "quarries",
}

BUILDING_NOTES = {
    "factories": "Makes 1,000💰 a turn.",
    "farms": "Grows 1,000🌾 a turn, enough to feed 1,000 people.",
    "sawmills": "Cuts 1,000🪵 a turn.",
    "quarries": "Digs 1,000🪨 a turn.",
    "depollutinators": "Scrubs the air clean.",
}

MARKET_PRICES = {"food": 0.8, "wood": 1.0, "stone": 1.2}

def nice(amount):
    return int(round(amount, -1)) if abs(amount) >= 100 else int(round(amount))

def scale_of(civ, name):
    if name == "population":
        return max(0.2, civ.population.value / 1000)
    if name not in SCALE_BY:
        return 1
    return max(1, getattr(civ, SCALE_BY[name]).value)

def build_effects(building):
    cost = 1 + 0.12 * building.value
    up = {}
    down = {}
    for name, base in (("money", building.price), ("wood", building.woodprice), ("stone", building.stoneprice)):
        if base:
            up[name] = -nice(base * cost)
            down[name] = nice(base * cost * 0.3)
    up[building.name] = 1
    up["available_land"] = -1
    down[building.name] = -1
    down["available_land"] = 1
    return {"up": up, "down": down}

def scaled(effects, civ, severity):
    result = {}
    for name, amount in effects.items():
        factor = scale_of(civ, name) * severity if name in SCALE_BY or name == "population" else 1
        if name == "build":
            result.update(build_effects(getattr(civ, amount))["up"])
        elif name == "buffs":
            result[name] = [
                (stat, kind, nice(value * scale_of(civ, stat) * severity) if kind == "add" else value, turns)
                for stat, kind, value, turns in amount
            ]
        elif name == "gamble":
            result[name] = [(weight, scaled(outcome, civ, severity)) for weight, outcome in amount]
        else:
            result[name] = nice(amount * factor)
    return result

def describe(effects):
    parts = []
    for name, amount in effects.items():
        if name == "buffs":
            for stat, kind, value, turns in amount:
                if kind == "add":
                    parts.append(f"{value:+,}".replace("-", "−") + f"{ICONS[stat]} a turn for {turns} turns")
                else:
                    parts.append(f"{ICONS[stat]} output x{value} for {turns} turns")
        elif name == "gamble":
            total = sum(weight for weight, outcome in amount)
            odds = " · ".join(f"{round(100 * weight / total)}% {describe(outcome)}" for weight, outcome in amount)
            parts.append(f"🎲 {odds}")
        else:
            parts.append(f"{amount:+,}".replace("-", "−") + ICONS[name])
    return " ".join(parts) or "nothing"

def sides_text(context, binary):
    if binary:
        return f"\n◀ Yes: {describe(context['yes'])}\n▶ No: {describe(context['no'])}"
    text = ""
    if "down" in context:
        text += f"\n◀ {describe(context['down'])} per notch"
    if "up" in context:
        text += f"\n▶ {describe(context['up'])} per notch"
    return text

def event_decision(civ, event, severity=1):
    context = {
        side: scaled(event[side], civ, severity)
        for side in ("always", "up", "down", "yes", "no")
        if side in event
    }
    text = event["text"]
    if "always" in context:
        text += f"\n⚠️ {describe(context['always'])}"
    text += sides_text(context, event["type"] == "binary")
    return Decision(title=event["title"], description=text, type=event["type"], context=context)

def build_decision(civ, building):
    context = build_effects(building)
    text = f"{BUILDING_NOTES[building.name]} Pollution {building.build_pollution:+}☁️ a turn each. You own {building.value}."
    text += sides_text(context, False)
    return Decision(
        title=f"{ICONS[building.name]} Build or demolish {building.name}?",
        description=text,
        type="scales",
        context=context,
    )

def trade_decision(civ, resource):
    mood = round(random.uniform(0.6, 1.5), 1)
    price = MARKET_PRICES[resource.name] * mood
    lot = nice(250 * scale_of(civ, resource.name))
    context = {
        "up": {"money": -nice(lot * price * 1.15), resource.name: lot},
        "down": {resource.name: -lot, "money": nice(lot * price * 0.85)},
    }
    if mood < 0.8:
        text = f"{resource.name.title()} is dirt cheap today ({mood}x the usual price)."
    elif mood > 1.2:
        text = f"{resource.name.title()} prices are through the roof ({mood}x the usual price)."
    else:
        text = f"A quiet day at the {resource.name} market."
    if resource.name == "food":
        text += " Your people eat 1🌾 each per turn."
    text += sides_text(context, False)
    return Decision(
        title=f"{ICONS[resource.name]} Market: {resource.name}",
        description=text,
        type="scales",
        context=context,
    )

def land_decision(civ, world):
    cost = nice(500 + 15 * max(0, 100 - world.wild_land.value))
    context = {
        "up": {"money": -cost, "wild_land": -1, "available_land": 1, "pollution": 1},
        "down": {"available_land": -1, "wild_land": 1, "happiness": 1},
    }
    text = f"Clear wild land for building, or give land back to nature. You have {civ.available_land.value} free and {world.wild_land.value} wild."
    text += sides_text(context, False)
    return Decision(title="🌲 Tame or rewild land?", description=text, type="scales", context=context)

def playable(decision, civ, world):
    sides = ("yes",) if decision.type == "binary" else ("up", "down")
    return any(affordable_notches(civ, world, decision.context[side], 1) >= 1 for side in sides if side in decision.context)

def build_need(civ, world, building):
    if building.name == "farms" and civ.farms.value * 1000 < civ.population.value * 1.2:
        return 4
    if building.name == "depollutinators" and world.pollution.value > 25:
        return 4
    return 1

def generate_generic_decisions(civ, world, turn, moves):
    builds = [build_decision(civ, building) for building in civ.buildings]
    others = [trade_decision(civ, resource) for resource in civ.resources] + [land_decision(civ, world)]
    land_need = 4 if civ.available_land.value < 3 else 1
    decisions = random.choices(others, [1, 1, 1, land_need])
    weights = [build_need(civ, world, building) for building in civ.buildings]
    while len(decisions) < 3:
        pick = random.choices(range(len(builds)), weights)[0]
        decisions.append(builds[pick])
        weights[pick] = 0

    pool = [event for event in event_catalogue.EVENTS if event.get("when", lambda civ, world: True)(civ, world)]
    pool.sort(key=lambda event: random.random() ** (1 / event.get("weight", 1)), reverse=True)
    wanted = max(3, moves)
    events = []
    for event in pool:
        decision = event_decision(civ, event)
        if playable(decision, civ, world):
            events.append(decision)
        if len(events) == wanted:
            break

    decisions += events
    random.shuffle(decisions)
    return decisions

def generate_special_decisions(civ, world, turn):
    severity = 1 + turn / 20
    return [event_decision(civ, crisis, severity) for crisis in event_catalogue.CRISES]

def crisis_chance(turn):
    return min(0.5, 0.2 + 0.01 * turn)
