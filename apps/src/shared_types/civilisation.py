from apps.src.shared_types.base_stat import *

class Civilisation():

    def __init__(self):
        self.population = Population('population',1000,self)
        #following generated with AI, using the above as template
        self.money = Money('money',1000,self)
        #Resources
        self.food = Food('food',1000,self)
        self.wood = Wood('wood',1000,self)
        self.stone = Stone('stone',1000,self)

        #Buildings
        self.factories = Factories('factories',1,self)
        self.farms = Farms('farms',1,self)
        self.sawmills = Sawmills('sawmills',1,self)
        self.quarries = Quarries('quarries',1,self)
        self.depollutinators = Depollutinators('depollutinators',0,self)

        self.available_land = Available_Land('available_land',10,self)
        self.happiness = Happiness('happiness',50,self)
        #end of AI usage

        self.stats = [self.population,self.money,self.food,self.wood,self.stone,self.happiness,
                          self.factories,self.farms,self.sawmills,self.quarries,
                          self.depollutinators,self.available_land]
        self.resources = [self.food,self.wood,self.stone]
        self.buildings = [self.factories,self.farms,self.sawmills,self.quarries]

    def update(self):
        for stat in self.stats:
            stat.update()

            stat.contribute()

    def pollute(self):
        for building in self.buildings:
            building.pollute(self)

    def get_move_count(self):

        alpha, beta = 0, 0

        # Amount of moves the player can make: 3 + Happiness weight (0.5 - 1.5) * population / 5000
        move_count = round(3 + (((self.happiness + 50) / 100) * (self.population / 5000)))

        move_count = int(move_count)

        return min(max(move_count, 1), 6)

    def isAlive(self):
        return self.population.value>0

    def get_stat(self):
        return {i.name:i.value for i in self.stats}