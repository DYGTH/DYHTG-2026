from enum import Enum

class Decision:

    def __init__(self, title: str, description: str, type: bool, context: tuple):

        self.title       = title
        self.description = description
        self.type        = type # use DecisionType enum
        self.context     = context

    @staticmethod
    def toJSON(decision: Decision, context: tuple):

        pass

class DecisionType(Enum):

    BINARY = 0
    SCALAR = 1