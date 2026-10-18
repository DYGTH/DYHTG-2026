from civilisation import Civilisation

""" Stat template """

class BaseStat:

    def __init__(self,name,value,civ):
            self.name = name
            self.value = value
            self.civ = civ
            self.addDict = {} #{'1':[50,3]}
            self.mulDict = {}
            self.price = 1
            self.count = 0
            self.contribution_type   = "add"
            self.contribution_factor = 0
    
    def add(self,adder):
        self.value += adder

    def mul(self,multiplier):
        self.value *= multiplier

    """ BASED ON MODIFIERS """
    def update(self):
        temp = set()
        for key,value in self.addDict.items():
            self.value += value[0]
            value[1] -= 1
            if value[1] == 0:
                temp.add(key)

        for i in temp:
            del self.addDict[i]

        temp = set()
        for key,value in self.mulDict.items():
            self.value *= value[0]
            value[1] -= 1
            if value[1] == 0:
                temp.add(key)

        for i in temp:
            del self.mulDict[i]

    """ BASED ON ATTRIBUTES (COUNT ETC.) """
    def contribute(self):

        contribution = self.contribution_factor * self.value
        self.contribution_type.add(contribution)

    def buffadd(self,value,turns):
        self.addDict[self.count] = [value,turns]
        self.count+=1

    def buffmul(self,value,turns):
        self.mulDict[self.count] = [value,turns]
        self.count+=1

# Stats for Civilisation
class Population(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.contribution_type = "mul"
        self.contribution_factor = (civ.food.value - self.value) / self.value

# Following class declarations at base level made by AI in format of above class

class Money(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.contribution_type = "add"
        self.contribution_factor = civ.factories.value * 1000 * (civ.factories.value * 1000)

class Food(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.contribution_type = "add"
        self.contribution_factor = civ.farms.value * 1000

class Wood(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.contribution_type = "add"
        self.contribution_factor = civ.sawmills.value * 1000

class Stone(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.contribution_type = "add"
        self.contribution_factor = civ.quarries.value * 1000

class Happiness(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.contribution_type = "add"
        self.contribution_factor = 

# End of AI use

"""
BUILDINGS
"""

class Building(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.build_pollution = 0

    def pollute(self,civ):
        civ.pollution.add(self.build_pollution)

class Factories(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 1000
        self.woodprice = 1000
        self.stoneprice = 1000
        self.build_pollution = 5

class Farms(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 0
        self.woodprice = 2000
        self.stoneprice = 0
        self.build_pollution = 2

        self.contribution_type   = "add"
        self.contribution_factor = 1000

class Sawmills(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 0
        self.woodprice = 2000
        self.stoneprice = 0
        self.build_pollution = 2

        self.contribution_type   = "add"
        self.contribution_factor = 1000

class Quarries(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 0
        self.woodprice = 0
        self.stoneprice = 2000
        self.build_pollution = 2

        self.contribution_type   = "add"
        self.contribution_factor = 1000

class Depollutinators(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 1000
        self.woodprice = 1000
        self.stoneprice = 1000
        self.build_pollution = -5

class Available_Land(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

# Stats for World
class Pollution(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

class Wild_Land(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)