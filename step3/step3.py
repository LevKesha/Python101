from FizzBuzzGame import FizzBuzzGame

conditions = ["one", "two", "three"]
game = FizzBuzzGame(conditions)

new_conditions = []

print("These are the available conditions: " + conditions.__str__())

for i in range(len(conditions)):
    user_input = input("Would you like to use this condition? Y/N " + conditions[i] + " ")
    if user_input == "Y":
        new_conditions.append(conditions[i])

add_condition = input("Would you like to add a new condition? Y/N ")
while add_condition == "Y":
    new_condition = input("Please write it ")
    new_conditions.append(new_condition)
    add_condition = input("Would you like to add a new condition? Y/N ")

print(new_conditions)
game = FizzBuzzGame(new_conditions)

