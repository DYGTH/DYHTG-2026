from pydantic import BaseModel

class Stat(BaseModel):
    value:float
    multiplier:float

    