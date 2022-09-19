from Rule import Rule


new_rule = input("Would you like to compose a new rule? Y/N ")
while new_rule == "Y":
    l_rule = input("Please write the first condition ")
    r_rule = input("Please write the second condition ")
    logic = input("Please write AND or OR ")
    rule = Rule(l_rule, r_rule, logic)
    print(rule.first + " " + rule.condition + " " + rule.second)
    new_rule = input("Would you like to compose a new rule? Y/N ")





