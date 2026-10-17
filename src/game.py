from shared_types.civilization import Civilization
from shared_types.world        import World

import exposure

def game_loop():

    # player civilization
    civ:   Civilization = Civilization()

    # ecosystem
    world: World        = World()

    turn:  int          = 0

    while (civ.isAlive()):

        turn += 1

        # decisions to choose from; limited amount
        decisions: list = generate_generic_decisions(civ, world)

        decisions.extend(generate_special_decisions(civ, world, turn))

        pass_decisions_to_frontend(decisions)

        while (True):

            if 

            # choices made will have immediate consequences as well as ongoing effects
            process_choices(choice)

        resolve_turn(civ, world, choices)


def generate_generic_decisions(civ: Civilization, world: World):

    decisions = []

    for res in civ.resources:

        # buy or sell resource

        pass

    for bul in civ.buildings:

        # 

        pass

    for res in world.resources:

        pass

    return decisions

def generate_special_decisions(civ: Civilization, world: World, turn: int):

    pass

def resolve_turn(civ: Civilization, world: World, choices: list):

    pass

def process_choices(choices: list):

    pass