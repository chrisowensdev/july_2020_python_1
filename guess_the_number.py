import random

print("I am thinking of a number between 1 and 10.\n")

random_number = random.randint(1, 10)

while True:
    user_input = int(input("Whats the numnber? "))
    if user_input == random_number:
        print("You win!")
        break
    elif user_input > random_number:
        print("%d is too high." % user_input)
    elif user_input < random_number:
        print("%d is too low." % user_input1)
    else:
        print("Nope, try again")
