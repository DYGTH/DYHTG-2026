from apps.src.shared_types.base_stat import *

class World():

    def __init__(self):
        self.pollution = Pollution('pollution',0,self)
        self.wild_land = Wild_Land('wild_land',100,self)
        self.stats = [self.pollution,self.wild_land]

    def update(self):
        for stat in self.stats:
            stat.update()

    def get_stat(self):
        return {i.name:i.value for i in self.stats}