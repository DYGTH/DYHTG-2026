from shared_types import Civilisation, World, Choice, Consequence, Decision

import decisions_generator
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
        decisions: list = decisions_generator.generate_generic_decisions(civ, world)
        decisions.extend( decisions_generator.generate_special_decisions(civ, world, turn))

        exposure.pass_decision_to_frontend(decision)


        while (True):

            choice = exposure.get_choice_from_frontend()

            if choice.type == 0: # choices completed
                break

            # choices made will have immediate consequences as well as ongoing effects
            consequence: Consequence = process_choice(civ, world, choice)

            exposure.pass_consequence_to_frontend(consequence)


        # modifiers and bonuses and stuff like that; maybe generate random events?
        resolve_turn(civ, world)

def resolve_turn(civ: Civilisation, world: World):

    civ  .update()
    world.update()

    #TODO

def process_choice(civ: Civilisation, world: World, choice: Choice):

    pass