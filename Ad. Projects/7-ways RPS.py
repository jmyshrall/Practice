""""

7-ways Rock,Paper,Scissors

Rules: 
ROCK POUNDS OUT FIRE, CRUSHES SCISSORS & SPONGE.
FIRE MELTS SCISSORS, BURNS PAPER & SPONGE.
SCISSORS SWISH THROUGH AIR, CUT PAPER & SPONGE.
SPONGE SOAKS PAPER, USES AIR POCKETS, ABSORBS WATER.
PAPER FANS AIR, COVERS ROCK, FLOATS ON WATER.
AIR BLOWS OUT FIRE, ERODES ROCK, EVAPORATES WATER.
WATER ERODES ROCK, PUTS OUT FIRE, RUSTS SCISSORS.

Comp 430, 3/20/2023
Justin Myshrall

"""""
import random

# create a list of possible choices
choices = ['rock', 'fire', 'scissors', 'sponge', 'paper', 'air', 'water']

# define the winning conditions
winning_conditions = {
    'rock': ['fire', 'scissors', 'sponge'],
    'fire': ['scissors', 'paper', 'sponge'],
    'scissors': ['paper', 'sponge', 'air'],
    'sponge': ['paper', 'air', 'water'],
    'paper': ['rock', 'air', 'water'],
    'air': ['fire', 'rock', 'water'],
    'water': ['fire', 'scissors', 'rock']
}

# ask the user to choose
user_choice = input("Choose rock, fire, scissors, sponge, paper, air, or water: ").lower()
# all inputs are lower-cased `.lower()`

# check if the user input is valid
if user_choice not in choices:
    print("Invalid choice. Please choose again.")
    # makes error case
else:
    # use random to choose the computer's choice
    computer_choice = random.choice(choices)

    # display the choices
    print(f"You chose {user_choice}.")
    # `f` makes f-string instead of concatenating the `print()` statement
    print(f"The computer chose {computer_choice}.")

    # check the result
    if user_choice == computer_choice:
        print("It's a tie")
    elif computer_choice in winning_conditions[user_choice]:
        # if `computer_choice` is in `winning_conditions` indexed by `user_choice` then you will win
        print("You win")
    else:
        print("You lose.")
