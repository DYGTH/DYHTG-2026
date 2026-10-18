import random

COSTS = (
    "money", "food", "wood", "stone", "available_land", "wild_land",
    "factories", "farms", "sawmills", "quarries", "depollutinators",
)

def find_stat(civ, world, name):
    return getattr(civ, name) if hasattr(civ, name) else getattr(world, name)

def affordable_notches(civ, world, effects, notches):
    for name, amount in effects.items():
        if name in COSTS and amount < 0:
            notches = min(notches, int(find_stat(civ, world, name).value // -amount))
    return notches

def apply_effects(civ, world, effects, notches):
    for name, amount in effects.items():
        if name == "buffs":
            for stat_name, kind, value, turns in amount:
                stat = find_stat(civ, world, stat_name)
                if kind == "add":
                    stat.buffadd(value * notches, turns)
                else:
                    stat.buffmul(value, turns)
        elif name == "gamble":
            for _ in range(notches):
                weights = [weight for weight, outcome in amount]
                outcomes = [outcome for weight, outcome in amount]
                apply_effects(civ, world, random.choices(outcomes, weights)[0], 1)
        else:
            find_stat(civ, world, name).add(amount * notches)
