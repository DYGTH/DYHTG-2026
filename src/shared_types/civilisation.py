from base_stat import *

class Civilisation():

    def __init__(self):
        self.population = Population('population',1000)
        #following generated with AI, using the above as template
        self.money = Money('money',1000)
        self.food = Food('food',1000)
        self.happiness = Happiness('happiness',100)
        self.factories = Factories('factories',1)
        self.farms = Farms('farms',1)
        #end of AI usage

        self.stats = [self.population,self.money,self.food,self.happiness,self.factories,self.farms]
        self.resources = [self.money,self.food]
        self.buildings = [self.factories,self.farms]

    def update(self):
        for stat in self.stats:
            stat.update()

    def isAlive(self):
        return self.population>0

    def get_stat(self):
        return {i.name:i.value for i in self.stats}