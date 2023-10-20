from ASCII import (rock, paper, scissors, won, lost, draw, error)
import random

print('Welcome to rock, paper and scissors game!')

choices = [rock, paper, scissors]

player_choice = choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper or "
                                  "2 for Scissors.\n"))]
print('Your choice')
print(player_choice)

computer_choice = choices[random.randint(0, 2)]
print('Computer choice')
print(computer_choice)

if player_choice == rock:
    if computer_choice == scissors:
        print(won)
    elif computer_choice == paper:
        print(lost)
    else:
        print(draw)
elif player_choice == scissors:
    if computer_choice == paper:
        print(won)
    elif computer_choice == rock:
        print(lost)
    else:
        print(draw)
elif player_choice == paper:
    if computer_choice == rock:
        print(won)
    elif computer_choice == scissors:
        print(lost)
    else:
        print(draw)
else:
    print(error)