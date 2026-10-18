""" Functions to save game to disk and load from disk. Supports a single save file. """

import os
import pickle
from   game import game_loop

savepath = os.path.join("..", "..", "..", "save")

def save_game(civ, world, turn_number):

    with open(os.path.join(savepath, "civsave.pkl"), "wb") as f:

        pickle.dump(civ, f)

    with open(os.path.join(savepath, "worldsave.pkl"), "wb") as f:

        pickle.dump(world, f)

    with open(os.path.join(savepath, "turn_number.txt"), "w") as f:

        f.write(str(turn_number))

def load_game():

    with open(os.path.join(savepath, "civsave.pkl"), "rb") as f:
        civ = pickle.load(f)

    with open(os.path.join(savepath, "worldsave.pkl"), "rb") as f:
        world = pickle.load(f)

    with open(os.path.join(savepath, "turn_number.txt"), "r") as f:
        turn_number = int(f.read())

    game_loop(civ, world, turn_number)