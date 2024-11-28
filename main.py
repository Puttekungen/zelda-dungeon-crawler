from func.trap import *
from func.shop import main as shop
import func.combat as combat
import func.inventory as inventory
import func.chest as chest
import func.stats as stats
from func.classes import Player
import func.boss as boss
import random
import sys

def get_user_input(text, valid_input):
    while True:
        user_input=input(f"{text}\n")
            
        for i in range(len(valid_input)):
            if str(valid_input[i]).lower()==user_input:
                return user_input
        print("Invalid input")

def door(player):
    print("Choose where to go")
    
    get_user_input("1.Left\n2.Forward\n3.Right\n",[1,2,3])

    if player.lvl >= 10:
        boss.boss(player) # runs final boss function
     # exits game after the boss is defeated

    #64% combat 20% trap 10% shop 10%chest
    rand = random.random()

    if rand<0.64:
        combat.combat(player)
    elif rand<0.80:
        trap(player)
    elif rand<0.90:
        chest.type(player)
    else:
        shop()

def print_intro():
    print("DUNGEON CRAWLER\n\n")

    meny = get_user_input("1.Start game\n2.Exit\n",["1","2"])
    if meny == "2":
        print("Exiting game...")
        sys.exit()
    elif meny == "1":
        print("Entering the dungeon...")   

    while True:
    
        name = input("Choose your name... ")
        player = Player(10, 20, 10, 5, name)
        
        while True:
            sure = input(f"You have entered '{player.name}', is this okay? [Y/n] ")
            if sure.lower() == "y" or sure == "":
                print("Entering game...\n")
                return player
            elif sure.lower() == "n":
                print("Choose again\n")
                break
            else:
                print("Invalid input")


player = print_intro()

while True:
    user_choice = get_user_input("Choose what to do\n1.Open door\n2.Inventory\n3.Stats\n4.Exit game\n",["1","2","3","4"])
    print("")
    
    if user_choice == "1":
        door(player)

    elif user_choice == "2":
        inventory.inventory(player)

    elif user_choice == "3":
        stats.stats(player)

    elif user_choice == "4":
        user_choice = get_user_input("Are you sure? Y/N",["Y","N"])

        if user_choice == "y":
            print("Exiting game...")
            sys.exit()