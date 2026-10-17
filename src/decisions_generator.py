from shared_types import Civilisation, Decision, World

from enum import Enum, auto

# Thanks to ChatGPT for enum syntax
class Identifiers(Enum):

    ARRAY_ADDITIVE = auto()

def generate_generic_decisions(civ: Civilisation, world: World):

    decisions = []

    for res in civ.resources:

        # buy or sell resource

        identifier = Identifiers.DICT_ADDITIVE

        encoding = (identifier, {res : res.value})

        decision = Decision(encoding=encoding)

        decisions.append(decision)

    for bul in civ.buildings:

        # build or demolish building

        pass

    for res in world.resources:

        pass

    return decisions

def generate_special_decisions(civ: Civilisation, world: World, turn: int):

    # enum to prevent duplicates

    pass