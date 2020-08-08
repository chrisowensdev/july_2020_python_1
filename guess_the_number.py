import random
import time
print("I am thinking of a number between 1 and 10.\n")

random_number = random.randint(1, 10)

play = True
while play == True:
    count = 1
    while True:
        user_input = int(input("Whats the numnber? "))
        if user_input == random_number:
            print("You win!")
            break
        elif count == 3:
            print("Too many guesses")
            break
        elif user_input > random_number:
            print("%d is too high." % user_input)
            count += 1
        elif user_input < random_number:
            print("%d is too low." % user_input)
            count += 1
        else:
            print("Nope try again")

    play_again = input("Do you want to play again? (y or n) ")
    if play_again == 'y':
        print("Good luck!")
        time.sleep(2)
    else:
        print("Have a nice day!")
        play = False
