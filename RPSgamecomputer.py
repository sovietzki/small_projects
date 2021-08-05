import random
game = ["rock", "paper", "scissors"]
player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins < winning_score and computer_wins < winning_score:
    print ()
    print(f"Player score: {player_wins}")
    print(f"Computer score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    print()
    p1 = input("(enter Player 1's choice): ")
    if p1 == "quit" or p1 == "q":
        break
    p2 = (random.choice(game))
    print("(Computer's choice): " + p2)
    print ("SHOOT!!!")
    if p1 == "rock":
        if p2 == p1:
            print ("It's a tie!")
        elif p2 == "paper":
            print("Computer wins!!!")
            computer_wins += 1
        elif p2 == "scissors":
            print("Player 1 wins!!!")
            player_wins += 1
        else:
            print ("You didn't type valid word")

    elif p1 == "scissors":
        if p2 == p1:
            print ("It's a tie!")
        elif p2 == "rock":
            print("Computer wins!!!")
            computer_wins += 1
        elif p2 == "paper":
            print("Player 1 wins!!!")
            player_wins += 1
        else:
            print ("You didn't type valid word")

    elif p1 == "paper":
        if p2 == p1:
            print ("It's a tie!")
        elif p2 == "scissors":
            print("Computer wins!!!")
            computer_wins += 1
        elif p2 == "rock":
            print("Player 1 wins!!!")
            player_wins += 1
        else:
            print ("You didn't type valid word")

    else:
        print("You didn't type valid word")        
print(f"Final scores... Player: {player_wins} Compter: {computer_wins}")
print()
if player_wins > computer_wins:
    print("Congratulations, you are better than the machine")
elif player_wins == computer_wins:
    print("It's a tie")
else:
    print("Maybe next time lad...")
