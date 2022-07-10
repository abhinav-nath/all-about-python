import os
import re
import random

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("\n")

    user_choice = input("Choose [R]ock, [P]aper or [S]cissors : ")

    if not re.match("[RrPpSs]", user_choice):
        print("Please choose a valid letter : [R]ock, [P]aper or [S]cissors")
        continue

    user_choice = str.upper(user_choice)
    print("You chose:", user_choice)

    choices = ['R', 'P', 'S']

    opponent_choice = random.choice(choices)

    print("I chose:", opponent_choice)

    if opponent_choice == user_choice:
        print("It's a Tie!")
    elif user_choice == 'R':
        if opponent_choice == 'S':
            print("Rock crushes Scissors, You win!")
        else:
            print("Paper covers Rock, I win!")
    elif user_choice == 'P':
        if opponent_choice == 'R':
            print("Paper covers Rock, You win!")
        else:
            print("Scissors cuts Paper, I win!")
    elif user_choice == 'S':
        if opponent_choice == 'P':
            print("Scissors cuts Paper, You win!")
        else:
            print("Rock crushes Scissors, I win!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break