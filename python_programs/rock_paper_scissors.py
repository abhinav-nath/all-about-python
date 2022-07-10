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

    print("You chose:", user_choice)

    choices = ['R', 'P', 'S']

    opponent_choice = random.choice(choices)

    print("I chose:", opponent_choice)

    if opponent_choice == str.upper(user_choice):
        print("It's a Tie!")
    elif opponent_choice == 'R' and user_choice.upper() == 'S':
        print("Rock crushes Scissors, I win!")
        continue
    elif opponent_choice == 'S' and user_choice.upper() == 'P':
        print("Scissors cuts Paper, I win!")
        continue
    elif opponent_choice == 'P' and user_choice.upper() == 'R':
        print("Paper covers Rock, I win!")
        continue
    else:
        print("You win!")