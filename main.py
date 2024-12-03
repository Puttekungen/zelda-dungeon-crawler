import func.trap as trap
import func.shop as shop
import func.combat as combat
import func.inventory as inventory
import func.chest as chest
import func.stats as stats
import func.classes as classes
import func.boss as boss
import random
import sys

def get_user_input(text, valid_input):
    while True:
        user_input=input(f"{text}\n")
        
        for i in range(len(valid_input)):
            if str(valid_input[i]).lower() == user_input:
                return user_input
        print("Invalid input")

def door(player):
    print("Choose where to go")
    get_user_input("1.Left\n2.Forward\n3.Right\n",[1,2,3])

    if player.lvl >= 10:
        boss.boss(player) # runs final boss function
        
    #45% combat 20% trap 15% shop 20%chest
    rand = random.random()
    if rand < 0.45:
        combat.combat(player)
    elif rand < 0.65:
        trap.trap(player)
    elif rand < 0.80:
        chest.type(player)
    else:
        shopping = shop.Shop()
        shopping.buy_item(player)

def print_intro():
    print("DUNGEON CRAWLER\n\n")

    meny = get_user_input("1.Start game\n2.Exit\n",["1","2"])
    if meny == "2":
        print("Exiting game...")
        sys.exit()
    elif meny == "1":
        print("Entering the dungeon...")   

    while True:
        player = classes.Player(10, 20, 1, 5, input("Choose your name... "))

        while True:
            decide = input(f"You have entered '{player.name}', is this okay? [Y/n] ")
            if decide.lower() == "y" or decide == "":
                print("Entering game...\n")
                return player
            elif decide.lower() == "n":
                print("Choose again\n")
                break
            else:
                print("Invalid input")


while True:
    player = print_intro()

    while player.hp > 0:
        user_choice = get_user_input("Choose what to do\n1.Open door\n2.Inventory\n3.Stats\n4.Exit game\n",["1","2","3","4"])
        
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
                

    if player.hp <= 0 :
        print("YOU DIED. GAME OVER!\n")
        input("press 'enter' to continue\n")
        print("Returning to main menu...\n")    