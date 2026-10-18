from shared_types import Civilisation, Decision, World

from enum import Enum, auto

# Thanks to ChatGPT for enum syntax
class Identifiers(Enum):

    BUYSELL      = auto()
    BUILDEMOLISH = auto()

def generate_generic_decisions(civ: Civilisation, world: World):

    decisions = []

    for res in civ.resources:

        # buy or sell resource

        identifier = Identifiers.BUYSELL

        context    = (identifier, res)

        decision   = Decision(
            title       = f"Buy/sell {res.name}?",
            description = f"Decide if you'd like to buy or sell {res.name}.",
            type        = "scales",
            context     = context
            )

        decisions.append(decision)

    for bul in civ.buildings:

        # build or demolish building

        identifier = Identifiers.BUILDEMOLISH

        context    = (identifier, bul)

        decision   = Decision(
            title       = f"Build/demolish {bul.name}?",
            description = f"Decide if you'd like to build or demolish {bul.name}.",
            type        = "scales",
            context     = context
            )

        decisions.append(decision)

    for res in world.resources:

        pass

    return decisions

def generate_special_decisions(civ: Civilisation, world: World, turn: int):

    decisions = []

    # enum to prevent duplicates
    
    # Turn wild land available
    
    identifier = Identifiers.TAMELAND
    
    context    = (identifier, world.wild_land)

    decision   = Decision(
        title       = f"Tame/Free wild land?",
        description = f"Decide if you'd like to tame wild lands and make them available to be built on or free claimed land.",
        type        = "scales",
        context     = context
        )

    decisions.append(decision)

    return decisions