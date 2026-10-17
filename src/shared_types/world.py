from base_stat import *

class World():

    def __init__(self):
        self.stats = []

    def update(self):
        for stat in self.stats:
            stat.update()

    def get_stat(self):
        return {i.name:i.value for i in self.stats}