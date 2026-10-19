from apps.src.shared_types import Civilisation, World, Choice, Decision
from save_and_load         import save_game

import decisions_generator
import effects
import exposure

import random

def start_game():

    # player civilization
    civ:   Civilisation = Civilisation()

    # ecosystem
    world: World        = World()

    turn:  int          = 0

    exposure.pass_civ_world_to_frontend(civ, world)

    game_loop(civ, world, turn)

def game_loop(civ, world, turn):

    while (civ.isAlive()):

            if turn >= 1:
                save_game(civ, world, turn)
    
            turn += 1
    
            exposure.pass_turn_to_frontend(turn)
    
            # move count will be kept track of by frontend
            moves = civ.get_move_count()

            # decisions to choose from; limited amount possible
            decisions: list         = decisions_generator.generate_generic_decisions(civ, world, turn, moves)
            special_decisions: list = decisions_generator.generate_special_decisions(civ, world, turn)

            start_stats = snapshot(civ, world)
    
            while (decisions):
    
                decision = decisions.pop(-1)
    
                exposure.pass_decision_to_frontend(decision)
    
                choice = exposure.get_choice_from_frontend()
    
                # choices made will have immediate consequences as well as ongoing effects
                process_choice(civ, world, choice)
    
                exposure.pass_civ_world_to_frontend(civ, world)
    
            # Random Special Event (RSP)
            if random.random() < decisions_generator.crisis_chance(turn):
                decision = random.choice(special_decisions)
                exposure.pass_decision_to_frontend(decision)
                
                choice = exposure.get_choice_from_frontend()
    
                # choices made will have immediate consequences as well as ongoing effects
                process_choice(civ, world, choice)
    
                exposure.pass_civ_world_to_frontend(civ, world)
    
            choice_stats = snapshot(civ, world)

            # modifiers and bonuses and stuff like that; maybe generate random events?
            resolve_turn(civ, world)

            exposure.pass_turn_summary_to_frontend(turn, start_stats, choice_stats, snapshot(civ, world))

            exposure.pass_civ_world_to_frontend(civ, world)


def snapshot(civ: Civilisation, world: World):

    return {**civ.get_stat(), **world.get_stat()}

def resolve_turn(civ: Civilisation, world: World):

    civ.update()
    civ.pollute(world)
    world.update()
    civ.suffer_pollution(world)

def process_choice(civ: Civilisation, world: World, choice: Choice):
    
    decision    = choice.decision
    choice_made = choice.choice_made
    context     = decision.context

    effects.apply_effects(civ, world, context.get("always", {}), 1)

    if decision.type == "binary":
        side    = "yes" if choice_made else "no"
        notches = 1
    else:
        side    = "up" if choice_made > 0 else "down"
        notches = int(abs(choice_made))

    if side not in context:
        return

    if decision.type == "scales" or side == "yes":
        notches = effects.affordable_notches(civ, world, context[side], notches)

    if notches > 0:
        effects.apply_effects(civ, world, context[side], notches)
