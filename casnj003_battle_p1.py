#
# File: casnj003_battle_p1.py
# Author: Noah Casey
# Email Id: casnj003
# Description: Dragon Battleground (created without the use of functions).
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Imports the provided dice.py module, as well as the built-in Random Module
import dice
import random

# Displays my details as per the PSP Assessment Requirements.
print("File\t : casnj003_battle_p1.py")
print("Author\t : Noah Casey")
print("This is my own work as defined by the\nUniversity's Academic Misconduct Policy.", end="\n\n")

game_counter: int = 0               # Keeps count of the amount of games played in succession (using Play Again) -> type: int
game_scores: list[int] = [0,0,0]    # [Win, Draw, Loss] -> type: list[int]
dragon_kills: int = 0               # Keeps count of the amount of times the Player kills the Dragon -> type: int

playing: str = ""
while playing != "y" and playing != "n":
    playing = input("Would you like to play Dragon Battleground [y|n]? ")

    if playing == "n":
        print("\n\nNo worries... you live to battle another day... :)")
    elif playing != "y":
        print("Please enter either 'y' or 'n'.", end="\n\n")

first_play = True   # Sets the whether it is the first run through of the game
while playing == "y":
    player_roll = [0, 0, 0, 0, 0]   # List containing the Player's randomly generated dice rolls
    dragon_roll = [0, 0, 0, 0, 0]   # List containing the Dragon's randomly generated dice rolls
    
    # The below Die Counters follow the alignment:
    #       [0, 0, 0, 0, 0, 0]
    #        1  2  3  4  5  6
    # Element [0] of each list will be used as though it is
    # equal to the die number | Die Number == 1 == Element [0]
    #
    # Each element will be added to, according to the amount of times
    # it appears in the appropriate Roll list
    player_die_counter = [0, 0, 0, 0, 0, 0] 
    dragon_die_counter = [0, 0, 0, 0, 0, 0]
    
    # Checks if this is the first run of the game
    #    TRUE = New Game    FALSE = Next Round
    if first_play:
        player_health = 100    # Sets the Player's health to 100
        dragon_health = 100    # Sets the Dragon's health to 100
        rounds_played = 1      # Sets the round number to 1

        game_counter += 1
        rounds_selected = input("\nPlease enter number of battle rounds: ")

        # Data validation ensuring the the user has inputted an integer between 1 and 5 inclusive
        while not rounds_selected.isdigit() or (int(rounds_selected) < 1 or int(rounds_selected) > 5):
            print("Must be between 1-5 inclusive.")
            rounds_selected = input("\nPlease enter number of battle rounds: ")
        else:
            first_play = False
            rounds_selected = int(rounds_selected)

        print(f"\n\n-- Battle -- Player versus Dragon: {rounds_selected} rounds --", end="\n\n\n")
    
    print(f"Round: {rounds_played}", end="\n\n")

    # Populating the player roll
    for index in range(len(player_roll)):
        roll = random.randint(1,6)
        player_roll[index] = roll
        player_die_counter[roll - 1] += 1

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
        if player_die_counter[0] == 3 or player_die_counter[2] == 3 or player_die_counter[4] == 3:
            player_damage = 0
            print("-- Swing and miss - no damage inflicted!")
        else:
            player_damage *= 3
            print("-- Critical hit - triple the damage!")

    # Pair
    elif 2 in player_die_counter:
        player_damage *= 2
        print("-- Hit - double the damage!")
    
    # IF no Pair or Three of a Kind, only print "-- Player has dealt..."
    print(f"-- Player has dealt {player_damage} damage", end="\n\n")
    dragon_health -= player_damage

    if dragon_health < 0:
        dragon_health = 0

    # Populating the dragon roll
    for index in range(len(dragon_roll)):
        roll = random.randint(1,6)
        dragon_roll[index] = roll
        dragon_die_counter[roll - 1] += 1

    print("Dragon rolled:")
    dice.display_dice(dragon_roll)
    print("\n")

    # Get sum of dice
    dragon_damage = 0
    for value in dragon_roll:
        dragon_damage += value
    
    # Determine Damage
    # Three of a Kind
    if 3 in dragon_die_counter or 4 in dragon_die_counter or 5 in dragon_die_counter:
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
    
    # IF no Pair or Three of a Kind, only print "-- Dragon has dealt..."
    print(f"-- Dragon has dealt {dragon_damage} damage", end="\n\n")
    player_health -= dragon_damage
    if player_health < 0:
        player_health = 0

    print(f"> Player - Damage taken: {dragon_damage} - Current health: {player_health}")
    print(f"> Dragon - Damage taken: {player_damage} - Current health: {dragon_health}", end="\n\n")

    rounds_played += 1

    # Is used to check if the game has finished and whether
    # to prompt if the user would like to play again
    play_again_prompt = False
    if dragon_health == 0 and player_health == 0:
        print("\n-- End of battle --", end="\n\n")
        print("-- Player has died!  :(", end="\n\n")
        print("-- Dragon has died!  :(", end="\n\n")
        print("** Draw! **", end="\n\n")
        game_scores[1] += 1
        play_again_prompt = True
    elif dragon_health == 0:
        print("\n-- End of battle --", end="\n\n")
        print("-- Dragon has died!  :(", end="\n\n")
        print("** Player wins! **", end="\n\n")
        game_scores[0] += 1
        play_again_prompt = True
    elif player_health == 0:
        print("-- End of battle --", end="\n\n")
        print("-- Player has died!  :(", end="\n\n")
        print("** Dragon wins! **", end="\n\n")
        game_scores[2] += 1
        play_again_prompt = True
    else:
        if rounds_played > rounds_selected:
            if player_health > dragon_health:
                print("\n-- End of battle --", end="\n\n")
                print("** Player wins! **", end="\n\n")
                game_scores[0] += 1
            elif dragon_health > player_health:
                print("\n-- End of battle --", end="\n\n")
                print("** Dragon wins! **", end="\n\n")
                game_scores[2] += 1
            elif player_health == dragon_health:
                print("** Draw! ** ", end="\n\n")
                game_scores[1] += 1
            play_again_prompt = True

    while play_again_prompt:
        play_again = input("\nPlay again [y|n]? ")

        if play_again == "y":
            first_play = True
            play_again_prompt = False
            game_counter += 1
        elif play_again == "n":
            playing = "n"
            play_again_prompt = False
        else:
            print("Please enter either 'y' or 'n'.")
else:
    if not first_play:
        print("\nGame Summary")
        print("============")
        print(f"You played {game_counter} games")
        print(f"\t|--> Games won:\t\t {game_scores[0]}")
        print(f"\t|--> Games lost:\t {game_scores[2]}")
        print(f"\t|--> Games drawn:\t {game_scores[1]}")
        print(f"\t|--> Dragons killed:\t {dragon_kills}")
        print("\nThanks for playing!")