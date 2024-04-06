#
# File: casnj003_battle_p1.py
# Author: Noah Casey
# Email Id: casnj003
# Description: Dragon Battleground.
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Dice module provided - display_dice() displays the dice face values
## import dice

## Prompt player to enter num rounds (between 1 and 5 - range(1,5))

## playerHP = 100, dragonHP = 100 - resets each round

## roll 5 dice each

## display rolls and damage dealt in round
    ## sum of 5 die values is damage inflicted
        ## If PAIR rolled, hit damage times 2 (sum * 2)
        ## If THREE OF A KIND rolled, critical hit (sum * 3)
        ## If 3 ONES, 3 THREES, or 3 FIVES rolled, miss (0 damage dealt)
        ## Else, damage == sum

## Display Damage Taken and Health

# Imports the provided dice.py Module.
import dice, random

# Displays my details as per the PSP Assessment Requirements.
print("File\t : casnj003_battle_p1.py")
print("Author\t : Noah Casey")
print("Email ID : casnj003")
print("This is my own work as defined by the\nUniversity's Academic Misconduct Policy.")

# Variable Definitions
game_counter = 0
game_scores = [0,0,0]    # [Win, Draw, Loss]
dragon_kills = 0

# The below list definitions all follow the alignment:
#       [0, 0, 0, 0, 0, 0]
#        0  1  2  3  4  5
# Element [0] of each list will not be utilised and is there
# to keep the alignment of 1 = 1, 2 = 2, etc.
player_roll = [0, 0, 0, 0, 0]
player_die_counter = [0, 0, 0, 0, 0, 0, 0]
dragon_roll = [0, 0, 0, 0, 0]
dragon_die_counter = [0, 0, 0, 0, 0, 0, 0]

playing = input("Would you like to play Dragon Battleground [y|n]? ")

if playing == "n":
    print("No worries... you live to battle another day.. :)")
elif playing != "y":
    print("Please enter either 'y' or 'n'.")

first_play = True
while playing == "y":
    if first_play:
        round_counter = input("Please enter number of battle rounds: ")

        while not round_counter.isdigit() or (int(round_counter) < 1 or int(round_counter) > 5):
            print("Must be between 1-5 inclusive.", end="\n\n")
            round_counter = input("Please enter number of battle rounds: ")
        else:
            first_play = False
            round_counter = int(round_counter)

    # Populating the player roll
    index = 0
    while index < len(player_roll):
        roll = random.randint(1,6)
        player_roll[index] = roll
        player_die_counter[roll] += 1
        index += 1

    print("Player rolled:")
    dice.display_dice(player_roll)
    
    # Get sum of dice
    player_damage = 0
    for value in player_roll:
        player_damage += value
    
    # Determine Damage
    # Three of a Kind
    if 3 in player_die_counter:
        if player_die_counter[1] == 3 or player_die_counter[3] == 3 or player_die_counter[5] == 3:
            player_damage = 0
        else:
            player_damage *= 3
    # Pair
    elif 2 in player_die_counter:
        player_damage *= 2

'''
    # Populating the dragon roll
    index = 0
    while index < len(dragon_roll):
        roll = random.randint(1,6)
        dragon_roll[index] = roll
        dragon_die_counter[roll] += 1
        index += 1

    print(f"Player Die Counter: {player_die_counter}")
    print(f"Dragon Die Counter: {dragon_die_counter}")
    break


while playing == "y":
    pass
else:
    print(f''
            Game Summary
            ============
            You played {game_counter} games
              |--> Games won:\t {game_scores[0]}
              |--> Games lost:\t {game_scores[2]}
              |--> Games drawn:\t {game_scores[1]}
              |--> Dragons killed:\t {dragon_kills}

            Thanks for playing!
          '')

'''