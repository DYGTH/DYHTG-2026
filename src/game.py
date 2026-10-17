from shared_types.civilization import Civilization
from shared_types.world        import World

def game_loop():

    # player civilization
    civ:   Civilization = Civilization()

    # ecosystem
    world: World        = World()

    while (civ.isAlive()):

        # decisions to choose from; limited amount
        decisions: list = generate_generic_decisions(civ, world)

        decisions.extend(generate_special_decisions(civ, world))

        decision = [decision.toJSON for decision in decisions]

        pass_decisions_to_frontend(decisions)

        choices = [] # list of tuples (Decision, True/False/scalar) [USE "is"!]

        # choices made will have immediate consequences as well as ongoing effects
        process_choices(choices)

        resolve_turn(civ, world, choices)


def generate_generic_decisions(civ: Civilization, world: World):

    for res in civ.resources:

        pass

    for res in world.resources:

        pass

def generate_special_decisions(civ: Civilization, world: World):

    pass

def resolve_turn(civ: Civilization, world: World, choices: list):

    pass

def process_choices(choices: list):

    pass

def pass_decisions_to_frontend(decisions: list):

    pass # no idea rn