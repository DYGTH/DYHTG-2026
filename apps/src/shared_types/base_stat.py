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
        if self.value <= 0:
            self.value = 0

    def mul(self,multiplier):
        self.value *= multiplier

    """ BASED ON MODIFIERS """
    def update(self):
        temp = set()
        for key,value in self.addDict.items():
            self.add(value[0])
            value[1] -= 1
            if value[1] == 0:
                temp.add(key)

        for i in temp:
            del self.addDict[i]

        temp = set()
        for key,value in self.mulDict.items():
            value[1] -= 1
            if value[1] <= 0:
                temp.add(key)

        for i in temp:
            del self.mulDict[i]

    def multiplier(self):
        result = 1
        for value in self.mulDict.values():
            result *= value[0]
        return result

    """ BASED ON ATTRIBUTES (COUNT ETC.) """
    def contribute(self):

        if self.contribution_type == "add":
            self.value += self.contribution_factor
        if self.contribution_type == "mul":
            self.value *= self.contribution_factor

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
        self.available = self.value

    def contribute(self):
        food = self.civ.food
        eaten = min(food.value, self.value)
        food.add(-eaten)
        self.civ.hungry = self.value - eaten
        if self.civ.hungry > 0:
            self.add(-self.civ.hungry / 2)
            return
        growth = self.value * 0.1 * (self.civ.happiness.value - 40) / 40
        self.add(min(growth, food.value))

# Following class declarations at base level made by AI in format of above class

class Money(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

    def contribute(self):
        self.value += self.civ.factories.value * 1000 * self.multiplier()
        upkeep = self.civ.upkeep()
        if self.value < upkeep:
            self.civ.happiness.add(-5)
        self.add(-upkeep)

class Food(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

    def contribute(self):
        self.value += self.civ.farms.value * 1000 * self.multiplier()

class Wood(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

    def contribute(self):
        self.value += self.civ.sawmills.value * 1000 * self.multiplier()

class Stone(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

    def contribute(self):
        self.value += self.civ.quarries.value * 1000 * self.multiplier()

class Happiness(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

    def add(self,adder):
        super().add(adder)
        self.value = min(self.value, 100)

    def contribute(self):
        target = 75 if self.civ.hungry == 0 else 10
        self.add((target - self.value) * 0.2)

# End of AI use

"""
BUILDINGS
"""

class Building(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.build_pollution = 0

    def pollute(self,world):
        world.pollution.add(self.build_pollution * self.value)

class Factories(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 800
        self.woodprice = 400
        self.stoneprice = 400
        self.build_pollution = 3

class Farms(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 400
        self.woodprice = 600
        self.stoneprice = 0
        self.build_pollution = 1

class Sawmills(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)
        self.price = 400
        self.woodprice = 0
        self.stoneprice = 600
        self.build_pollution = 2

class Quarries(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.price = 400
        self.woodprice = 600
        self.stoneprice = 0
        self.build_pollution = 2

class Depollutinators(Building):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.price = 1200
        self.woodprice = 600
        self.stoneprice = 800
        self.build_pollution = -6

class Available_Land(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

        self.build_pollution = -2

# Stats for World
class Pollution(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)

    def contribute(self):
        self.value = max(0, self.value * 0.85 - self.civ.wild_land.value * 0.05)

class Wild_Land(BaseStat):

    def __init__(self, name, value, civ):
        super().__init__(name, value, civ)