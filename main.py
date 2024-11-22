import func.trap as trap
import func.shop as shop
import func.combat as combat
import func.inventory as inventory
import func.chest as chest
import func.classes as classes
import random
import sys

def random_room():
    print("Choose where to go")
    
    user_input = get_user_input("1.Left\n2.Right\n3.Forward",[1,2,3])


    #33% combat 25% shop 15% chest 10%trap
    rand=random.random()

    if rand<0.33:
        combat.combat()
    elif rand<0.66:
        shop.shop()
    elif rand<0.75:
        chest.type()
    elif rand<=1:
        trap.trap()

def print_intro():
    print("DUNGEON CRAWLER")

    print("\n")

    meny = get_user_input("1.Start game\n2.Exit",["1","2"])
    if meny == "2":
        print("Exiting game...")
        sys.exit()
    elif meny == "1":
        print("Entering the dungeon...")   

    print("intro")
    classes.player.name = input("Choose name... ")
    print(classes.player.name)
    print("begin")

def get_user_input(text, valid_input):
    while True:

        user_input=input(f"{text}\n")
            
        for i in range(len(valid_input)):

            if str(valid_input[i]).lower()==user_input:
                return user_input

print_intro()

while True:
    user_choice = get_user_input("1.Open door\n2.Inventory\n3.Exit game",["1","2","3"])
    
    if user_choice == "1":
        random_room()

    elif user_choice == "2":
        inventory.inventory()

    elif user_choice == "3":
        user_choice = get_user_input("Are you sure? Y/N",["Y","N"])

        if user_choice == "y":
            print("Exiting game...")
            sys.exit()