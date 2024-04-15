#
# File: casnj003_battle_p1.py
# Author: Noah Casey
# Email Id: casnj003
# Description: Dragon Battleground (created with the use of functions).
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

# Imports the provided dice.py module, as well as the built-in Random Module
import dice, random

game_counter = 0         # Keeps count of the amount of games played in succession (using Play Again)
game_scores = [0,0,0]    # [Win, Draw, Loss]
dragon_kills = 0         # Keeps count of the amount of times the Player kills the Dragon

# Displays my details as per the PSP Assessment Requirements.
def display_details():
    print("File\t : casnj003_battle_p1.py")
    print("Author\t : Noah Casey")
    print("Email ID : casnj003")
    print("This is my own work as defined by the\nUniversity's Academic Misconduct Policy.", end="\n\n")

def roll_die():
    return random.randint(1,6)

def roll_damage(max_dice: int) -> list:
        roll_list = []
        for index in range(max_dice):
             roll_list.append(roll_die())

        return roll_list


def calculate_damage(roll: list) -> int:
    damage = 0
    die_counter = [0, 0, 0, 0, 0, 0, 0]
    for value in roll:
        damage += value
        die_counter[value] += 1

    if 3 in die_counter or 4 in die_counter or 5 in die_counter:
        if die_counter[1] == 3 or die_counter[3] == 3 or die_counter[5] == 3:
            damage = 0
            print("-- Swing and miss - no damage inflicted!")
        else:
            damage *= 3
            print("-- Critical hit - triple the damage!")

    # Pair
    elif 2 in die_counter:
        damage *= 2
        print("-- Hit - double the damage!")

    return damage


display_details()

playing = input("Would you like to play Dragon Battleground [y|n]? ")

if playing == "n":
    print("\n\nNo worries... you live to battle another day... :)")
elif playing != "y":
    print("Please enter either 'y' or 'n'.", end="\n\n")

while playing != "y" and playing != "n":
    playing = input("Would you like to play Dragon Battleground [y|n]? ")
    if playing == "n":
        print("\n\nNo worries... you live to battle another day... :\)")
    elif playing != "y":
        print("Please enter either 'y' or 'n'.", end="\n\n")

first_play = True
while playing == "y":
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

    player_roll = roll_damage(5)
    print("Player rolled:")
    dice.display_dice(player_roll)
    print("\n")

    player_damage = calculate_damage(player_roll)

    print(f"-- Player has dealt {player_damage} damage", end="\n\n")
    dragon_health -= player_damage

    if dragon_health < 0:
        dragon_health = 0
    
    dragon_roll = roll_damage(5)
    print("Dragon rolled:")
    dice.display_dice(dragon_roll)
    print("\n")

    dragon_damage = calculate_damage(dragon_roll)
    
    print(f"-- Dragon dealt {dragon_damage} damage", end="\n\n")
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
        print("-- Player has died!  :\(", end="\n\n")
        print("-- Dragon has died!  :\(", end="\n\n")
        print("** Draw! **", end="\n\n")
        game_scores[1] += 1
        play_again_prompt = True
    elif dragon_health == 0:
        print("\n-- End of battle --", end="\n\n")
        print("-- Dragon has died!  :\(", end="\n\n")
        print("** Player wins! **", end="\n\n")
        game_scores[0] += 1
        play_again_prompt = True
    elif player_health == 0:
        print("-- End of battle --", end="\n\n")
        print("-- Player has died!  :\(", end="\n\n")
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
    if not first_play:
        print("\nGame Summary")
        print("============")
        print(f"You played {game_counter} games")
        print(f"\t|--> Games won:\t\t {game_scores[0]}")
        print(f"\t|--> Games lost:\t {game_scores[2]}")
        print(f"\t|--> Games drawn:\t {game_scores[1]}")
        print(f"\t|--> Dragons killed:\t {dragon_kills}")
        print("\nThanks for playing!")