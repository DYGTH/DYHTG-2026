from pydantic import BaseModel

class Population(BaseModel):
    value:float
    mult:float

#Used AI to create following classes based on above model
class Money(BaseModel):
    value:float
    add:float

class Food(BaseModel):
    value:float
    add:float

class Happiness(BaseModel):
    value:float
    mult:float

class Factories(BaseModel):
    value:float

class Farms(BaseModel):
    value:float

class Environment(BaseModel):
    value:float
    mult:float