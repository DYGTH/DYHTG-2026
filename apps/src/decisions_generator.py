from apps.src.shared_types import Civilisation, Decision, World

from enum   import Enum, auto
from random import randint

# Thanks to ChatGPT for enum syntax
class Identifiers(Enum):

    BUYSELL      = auto()
    BUILDEMOLISH = auto()
    TAMELAND = auto()
    SPECIAL = auto()

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

    # TODO
    # missing for loop?: <- This makes no sense, there's nothing to loop
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

    # mangle decisions list
    for _ in range(len(decisions) * 2):

        n, m = randint(0, 50) % len(decisions), randint(0, 50) % len(decisions)

        decisions[n], decisions[m] = decisions[m], decisions[n]
    
    return decisions[:7]

def generate_special_decisions(civ: Civilisation, world: World, turn: int):

    decisions = []

    # enum to prevent duplicates

    for turns in range(1,6):
    
        identifier = Identifiers.SPECIAL

        # Drought Special Decision

        type = 'mul'

        scale = 0.8
        
        context    = (identifier,type,civ.food,scale,turns,civ.farms)

        decision   = Decision(
            title       = f"Drought! (0.8x multiplier on food for {turns} turns)",
            description = f"Will you buy food or build Farms",
            type        = "scales",
            context     = context
            )

        decisions.append(decision)

        # Wood Fungus Special Decision

        type = 'mul'
        
        scale = 0.8
        
        context    = (identifier,type,civ.wood,scale,turns,civ.sawmills)

        decision   = Decision(
            title       = f"A wood fungus is eating the trees (0.8x multiplier on food for {turns} turns)",
            description = f"Will you buy wood or build Saw Mills",
            type        = "scales",
            context     = context
            )

        decisions.append(decision)

        # Mineshaft Collapse Special Decision
        
        type = 'mul'
        
        scale = 0.8
        
        context    = (identifier,type,civ.stone,scale,turns,civ.quarries)

        decision   = Decision(
            title       = f"A huge mineshaft collapsed and will take multiple days to rebuild (0.8x multiplier on food for {turns} turns)",
            description = f"Will you buy stone or build Quarries",
            type        = "scales",
            context     = context
            )

        decisions.append(decision)

    return decisions