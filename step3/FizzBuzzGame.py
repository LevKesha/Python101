def get_rules(self):
    return self.conditions


def set_rules(self, rules):
    self.conditions = rules


class FizzBuzzGame:
    def __init__(self, rules):
        self.rules = rules

