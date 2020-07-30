coins = 0
user_input = "yes"
while user_input == "yes":
    print("You have " + str(coins) + " coins.")
    user_input = (input("Do you want another? "))
    coins += 1
    if user_input == "no":
        print("Bye")
        break
