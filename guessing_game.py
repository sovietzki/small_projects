import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

user_choice = None
while user_choice != random_number:
    print()
    user_choice = int(input("Please pick your number from 1 to 10: "))
    if user_choice < random_number:      
        print()
        print("That's too low, aim higher")
        
    elif user_choice > random_number:
        print()
        print("That's too high, but I aprreciate your confidence")
       
    else:
        
        print()
        print("Congratulations, you have guessed it!!!")
        print()
        play_again = input("Do you want to play again? [y/n] ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            user_choice = None
        else:
            print()
            print("Thank you for playing")
            break               
print()



