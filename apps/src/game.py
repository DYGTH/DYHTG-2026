from shared_types import Civilisation, World, Choice, Decision

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

        # decisions to choose from; limited amount possible
        decisions: list = decisions_generator.generate_generic_decisions(civ, world)
        decisions.extend( decisions_generator.generate_special_decisions(civ, world, turn))


        while (decisions):

            decision = decisions.pop(-1)

            exposure.pass_decision_to_frontend(decision)

            choice = exposure.get_choice_from_frontend()

            # choices made will have immediate consequences as well as ongoing effects
            process_choice(civ, world, choice)

            exposure.pass_civ_world_to_frontend(civ, world)


        # modifiers and bonuses and stuff like that; maybe generate random events?
        resolve_turn(civ, world)


def resolve_turn(civ: Civilisation, world: World):

    civ  .update()
    civ  .pollute()
    world.update()

    #TODO

def process_choice(civ: Civilisation, world: World, choice: Choice):
    
    decision    = choice.decision
    choice_made = choice.choice_made
    context     = decision.context

    match context[0]:
        
        case decisions_generator.Identifiers.BUYSELL:

            context[1].add(choice_made)
            civ.money.add(-(context[1].price * choice_made))

        case decisions_generator.Identifiers.BUILDEMOLISH:

            if choice_made >= 0:
                context[1].add(choice_made)
                civ.money.add(-(context[1].price * choice_made))
                civ.wood.add(-(context[1].woodprice * choice_made))
                civ.stone.add(-(context[1].stoneprice * choice_made))
                civ.available_land.add(-choice_made)
            else:
                context[1].add(-choice_made)
                civ.available_land.add(choice_made)

        case decisions_generator.Identifiers.TAMELAND:

            context[1].add(-choice_made)
            civ.available_land.add(choice_made)
            world.pollution.add(choice_made)