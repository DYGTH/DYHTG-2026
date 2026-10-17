class Base_stat:

    def __init__(self,name,value):
            self.name = name
            self.value = value
            self.addDict = {} #{'1':[50,3]}
            self.mulDict = {}
            self.count = 0
    
    def add(self,adder):
        self.value += adder

    def mul(self,multiplier):
        self.value *= multiplier

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

    def buffadd(self,value,turns):
        self.addDict[self.count] = [value,turns]
        self.count+=1

    def buffmul(self,value,turns):
        self.mulDict[self.count] = [value,turns]
        self.count+=1

class Population(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

# Following class declarations in made by AI in format of above class

class Money(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

class Food(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

class Happiness(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

class Factories(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

class Farms(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

# End of AI use

class Available_Land(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

class Pollution(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)

class Wild_Land(Base_stat):

    def __init__(self, name, value):
        super().__init__(name, value)


money = Money("money", 500)

money.buffadd(50,1)
money.buffmul(2,3)
for i in range(4):
     money.update()
     print(money.value)