from shared_types import Civilisation, World, Choice

import exposure

def game_loop():

    # player civilization
    civ:   Civilisation = Civilisation()

    # ecosystem
    world: World        = World()

    turn:  int          = 0

    while (civ.isAlive()):

        turn += 1

        # decisions to choose from; limited amount
        decisions: list = generate_generic_decisions(civ, world)
        decisions.extend( generate_special_decisions(civ, world, turn))

        exposure.pass_decisions_to_frontend(decisions)


        while (True):

            choice = exposure.get_choice_from_frontend()

            if choice.type == 0: # choices completed
                break

            # choices made will have immediate consequences as well as ongoing effects
            process_choice(civ, world, choice)


        # modifiers and bonuses and stuff like that; maybe generate random events?
        resolve_turn(civ, world)


def generate_generic_decisions(civ: Civilisation, world: World):

    decisions = []

    for res in civ.resources:

        # buy or sell resource

        pass

    for bul in civ.buildings:

        # build or demolish building

        pass

    for res in world.resources:

        pass

    return decisions

def generate_special_decisions(civ: Civilisation, world: World, turn: int):

    # enum to prevent duplicates

    pass

def resolve_turn(civ: Civilisation, world: World):

    civ  .update()
    world.update()

    #TODO

def process_choice(civ: Civilisation, world: World, choice: Choice):

    pass