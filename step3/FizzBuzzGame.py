def get_rules(self):
    return self.conditions


def set_rules(self, conditions):
    self.conditions = conditions


class FizzBuzzGame:
    def __init__(self, conditions):
        self.rules = conditions

