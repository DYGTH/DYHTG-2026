from apps.src.shared_types.decision import Decision

class Choice():

    def __init__(self, decision: Decision, choice_made):
        self.decision = decision
        self.choice_made = choice_made
