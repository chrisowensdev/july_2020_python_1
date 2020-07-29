user_input = int(input("Guess a number 5-50: "))
magic_number = 6

# if user_input == magic_number:
#     print("ARE YOU A MIND READER!?!?")
# elif user_input > 50:
#     print("Guess was too high!")
# elif user_input < 5:
#     print("Guess was too low.")
# else:
#     print("Sorry. Try again.")

if user_input == magin_number:
    print("ARE YOU A MINDREADER!?!?!")
elif (user_input < 5) or (user_input > 50):
    print("YOU'RE OUT OF RANGE!")
else:
    print("Sorry. Try again.")
