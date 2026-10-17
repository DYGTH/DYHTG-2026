from base_stat import *

class Civilisation():

    def __init__(self):
        self.population = Population('population',1000)
        #following generated with AI, using the above as template
        self.money = Money('money',1000)
        self.food = Food('food',1000)
        self.wood = Wood('wood',1000)
        self.stone = Stone('stone',1000)
        self.happiness = Happiness('happiness',100)
        self.factories = Factories('factories',1)
        self.farms = Farms('farms',1)
        self.sawmills = Sawmills('sawmills',1)
        self.quarries = Quarries('quarries',1)
        self.available_land = Available_Land('available_land',10)
        #end of AI usage

        self.stats = [self.population,self.money,self.food,self.happiness,self.factories,self.farms]
        self.resources = [self.food,self.wood,self.stone]
        self.buildings = [self.factories,self.farms,self.sawmills,self.quarries]

    def update(self):
        for stat in self.stats:
            stat.update()

    def isAlive(self):
        return self.population.value>0

    def get_stat(self):
        return {i.name:i.value for i in self.stats}