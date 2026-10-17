from decision import Decision

class Choice():

    def __init__(self, decision: Decision, type:int=1):

        self.type = type # 0 = out of choices, 1 = choice
