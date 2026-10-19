import random

def find_stat(civ, world, name):
    return getattr(civ, name) if hasattr(civ, name) else getattr(world, name)

def turn_losses(effects):
    losses = {}
    for stat_name, kind, value, turns in effects.get("buffs", []):
        if kind == "add" and value < 0:
            losses[stat_name] = losses.get(stat_name, 0) - value
    return losses

def active_loss(stat):
    return -sum(value for value, turns in stat.addDict.values() if value < 0)

def affordable_notches(civ, world, effects, notches):
    for name, amount in effects.items():
        if name not in ("buffs", "gamble") and amount < 0:
            notches = min(notches, int(find_stat(civ, world, name).value // -amount))
    for name, loss in turn_losses(effects).items():
        stat = find_stat(civ, world, name)
        notches = min(notches, int(max(0, stat.value - active_loss(stat)) // loss))
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
