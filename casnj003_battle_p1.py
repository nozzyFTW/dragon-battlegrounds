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
print("This is my own work as defined by the\nUniversity's Academic Misconduct Policy.", end="\n\n")

# Variable Definitions
game_counter = 0
game_scores = [0,0,0]    # [Win, Draw, Loss]
dragon_kills = 0




playing = input("Would you like to play Dragon Battleground [y|n]? ")

if playing == "n":
    print("\n\nNo worries... you live to battle another day... :)")
elif playing != "y":
    print("Please enter either 'y' or 'n'.")

while playing != "y" and playing != "n":
    playing = input("Would you like to play Dragon Battleground [y|n]? ")
    if playing == "n":
        print("\n\nNo worries... you live to battle another day... :)")
    elif playing != "y":
        print("Please enter either 'y' or 'n'.")

first_play = True
while playing == "y":
    player_roll = [0, 0, 0, 0, 0]
    dragon_roll = [0, 0, 0, 0, 0]
    
    # The below Die Counters follow the alignment:
    #       [0, 0, 0, 0, 0, 0, 0]
    #        0  1  2  3  4  5  6
    # Element [0] of each list will not be utilised and is there
    # to keep the alignment of 1 = 1, 2 = 2, etc.
    player_die_counter = [0, 0, 0, 0, 0, 0, 0]
    dragon_die_counter = [0, 0, 0, 0, 0, 0, 0]
    
    if first_play:
        player_health = 100
        dragon_health = 100
        rounds_played = 1

        rounds_selected = input("\nPlease enter number of battle rounds: ")

        while not rounds_selected.isdigit() or (int(rounds_selected) < 1 or int(rounds_selected) > 5):
            print("Must be between 1-5 inclusive.")
            rounds_selected = input("\nPlease enter number of battle rounds: ")
        else:
            first_play = False
            rounds_selected = int(rounds_selected)

        print(f"\n\n-- Battle -- Plater versus Dragon: {rounds_selected} rounds --", end="\n\n\n")
    
    print(f"Round: {rounds_played}", end="\n\n")

    # Populating the player roll
    index = 0
    while index < len(player_roll):
        roll = random.randint(1,6)
        player_roll[index] = roll
        player_die_counter[roll] += 1
        index += 1

    print("Player rolled:")
    dice.display_dice(player_roll)
    print("\n")
    
    # Get sum of dice
    player_damage = 0
    for value in player_roll:
        player_damage += value
    
    # Determine Damage
    # Three of a Kind
    if 3 in player_die_counter:
        if player_die_counter[1] == 3 or player_die_counter[3] == 3 or player_die_counter[5] == 3:
            player_damage = 0
            print("-- Swing and miss - no damage inflicted!")
        else:
            player_damage *= 3
            print("-- Critical hit - triple the damage!")
    # Pair
    elif 2 in player_die_counter:
        player_damage *= 2
        print("-- Hit - double the damage!")
    
    # IF no Pairs of Three of a Kinds, only print "-- Player has dealt..."
    print(f"-- Player has dealt {player_damage} damage", end="\n\n")
    dragon_health -= player_damage

    if dragon_health < 0:
        dragon_health = 0

    # Populating the dragon roll
    index = 0
    while index < len(dragon_roll):
        roll = random.randint(1,6)
        dragon_roll[index] = roll
        dragon_die_counter[roll] += 1
        index += 1

    print("Dragon rolled:")
    dice.display_dice(dragon_roll)
    print("\n")

    # Get sum of dice
    dragon_damage = 0
    for value in dragon_roll:
        dragon_damage += value
    
    # Determine Damage
    # Three of a Kind
    if 3 in dragon_die_counter:
        if dragon_die_counter[1] == 3 or dragon_die_counter[3] == 3 or dragon_die_counter[5] == 3:
            dragon_damage = 0
            print("-- Swing and miss - no damage inflicted!")
        else:
            dragon_damage *= 3
            print("-- Critical hit - triple the damage!")
    # Pair
    elif 2 in dragon_die_counter:
        dragon_damage *= 2
        print("-- Hit - double the damage!")
    
    # IF no Pairs of Three of a Kinds, only print "-- Dragon has dealt..."
    print(f"-- Dragon has dealt {dragon_damage} damage", end="\n\n")
    player_health -= dragon_damage
    if player_health < 0:
        player_health = 0

    print(f"> Player - Damage taken: {dragon_damage} - Current health: {player_health}")
    print(f"> Dragon - Damage taken: {player_damage} - Current health: {dragon_health}", end="\n\n")

    rounds_played += 1
    play_again_prompt = False
    if dragon_health == 0 or (player_health > dragon_health and rounds_played > rounds_selected):
        print("\n-- End of battle --", end="\n\n")
        print("** Player wins! **", end="\n\n")
        game_scores[0] += 1
        play_again_prompt = True
    elif player_health == 0 or (dragon_health > player_health and rounds_played > rounds_selected):
        print("-- End of battle --", end="\n\n")
        print("** Dragon wins! **", end="\n\n")
        game_scores[2] += 1
        play_again_prompt = True
    elif player_health == dragon_health and rounds_played > rounds_selected:
        print("** Draw! ** ", end="\n\n")
        game_scores[1] += 1
        play_again_prompt = True

    if play_again_prompt:
        play_again = input("\nPlay again [y|n]? ")

        if play_again == "y":
            first_play = True
        elif play_again == "n":
            playing = "n"
        elif play_again != "y":
            print("Please enter either 'y' or 'n'.")

        while play_again != "y" and play_again != "n":
            play_again = input("Play again [y|n]? ")
            if play_again == "y":
                first_play = True
                game_counter += 1
            elif play_again == "n":
                playing = "n"
            elif play_again != "y":
                print("Please enter either 'y' or 'n'.")
else:
    print(f'''
          
Game Summary
============
You played {game_counter} games
  |--> Games won:\t {game_scores[0]}
  |--> Games lost:\t {game_scores[2]}
  |--> Games drawn:\t {game_scores[1]}
  |--> Dragons killed:\t {dragon_kills}

Thanks for playing!

          ''')