""" Functions to save game to disk and load from disk. Supports a single save file. """

import os
import pickle

savepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "save")

def save_game(civ, world, turn_number):

    os.makedirs(savepath, exist_ok=True)

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

    return civ, world, turn_number