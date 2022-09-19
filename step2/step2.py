outputs = ["console", "email", "file"]

user_input = input("Please select output method or press 991 for adding new method" + outputs.__str__()+" ")
while user_input == "991":
    new_out = input("Please enter a new output method ")
    outputs.append(new_out)
    user_input = input("Please select output method or press 991 for adding new method" + outputs.__str__() + " ")


print("chosen output method is: " + user_input)


for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)




