import func.trap as trap
import func.shop as shop
import func.combat as combat
import func.inventory as inventory
import func.chest as chest
import func.classes as classes
import random
import sys

def random_room():
    #33% combat 25% shop 15% chest 10%trap
    rand=random.random()

    if rand<0.33:
        combat.combat()
    elif rand<0.66:
        shop.shop()
    elif rand<=0.75:
        chest.chest()
    elif rand<=1:
        trap.trap()



meny = classes.user_input("1.Start game\n2.Exit",["1","2"])
if meny == "2":
    print("Exiting game...")
    sys.exit()
elif meny == "1":
    print("Entering the dungeon...")   

print("intro")

classes.player.name = classes.user_input("Choose name... ")

print(classes.player.name)

print("begin")


while True:
    choice = classes.user_input("1.Open door\n2.Inventory\n3.Exit game\n",["1","2","3"])

    if choice == "1":
        random_room()
    elif choice == "2":
        inventory.inventory()
    elif choice == "3":
        end = classes.user_input("Are you sure? Y/N ",["Y","N"])
        if end == "y":
            print("Exiting game...")
            sys.exit()
        elif end == "n":
            print("Returning to game...")