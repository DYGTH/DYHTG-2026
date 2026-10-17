from shared_types.civilization import Civilization
from shared_types.world        import World

def game_loop():

    # player civilization
    civ:   Civilization = Civilization()

    # ecosystem
    world: World        = World()

    while (civ.isAlive()):

        # decisions to choose from; limited amount
        decisions_candidates: list = generate_decisions(civ, world)

        # select decisions to make
        decisions: list = select_decisions(decisions_candidates)

        # a decision made is a choice
        choices: list = make_choices(devilization()cisions)

        new_civ, new_world = resolve_turn(civ, world, choices)


def generate_decisions(civ: Civilization, world: World):

    pass

def resolve_turn(civ: Civilization, world: World, choices: list):

    pass