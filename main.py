from func.trap import *
import func.shop as shop
import func.combat as combat
import func.inventory as inventory
import func.chest as chest
import func.stats as stats
from func.classes import Player
import random
import sys

def random_room(player):
    print("Choose where to go")
    
    user_input = get_user_input("1.Left\n2.Forward\n3.Right\n",[1,2,3])


    #64% combat 20% trap 10% shop 10%chest
    rand = random.random()

    if rand<0.64:
        combat.combat(player)
    elif rand<0.80:
        trap(player)
    elif rand<0.90:
        chest.type(player)
    else:
        shop.shop(player)

def print_intro(player):
    print("DUNGEON CRAWLER\n\n")

    meny = get_user_input("1.Start game\n2.Exit\n",["1","2"])
    if meny == "2":
        print("Exiting game...")
        sys.exit()
    elif meny == "1":
        print("Entering the dungeon...")   

    while True:
    
        name = input("Choose your name... ")

        player = Player(10, 20, 2, 5, name)
        
        while True:
            sure = input(f"You have entered '{player.name}', is this okay? [Y/N] ")
            if sure.lower() == "y":
                print("Entering game...\n")
                return player
            elif sure.lower() == "n":
                print("Choose again\n")
                break
            else:
                print("Invalid input")


def get_user_input(text, valid_input):
    while True:

        user_input=input(f"{text}\n")
            
        for i in range(len(valid_input)):

            if str(valid_input[i]).lower()==user_input:
                return user_input



global player = Player()

print_intro()

while True:
    user_choice = get_user_input("1.Open door\n2.Inventory\n3.Stats\n4.Exit game\n",["1","2","3","4"])
    print("")
    
    if user_choice == "1":
        random_room(player)

    elif user_choice == "2":
        inventory.inventory()

    elif user_choice == "3":
        stats.stats(player)

    elif user_choice == "4":
        user_choice = get_user_input("Are you sure? Y/N",["Y","N"])

        if user_choice == "y":
            print("Exiting game...")
            sys.exit()