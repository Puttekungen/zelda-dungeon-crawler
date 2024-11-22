from func.trap import traps, trap
import func.shop as shop
import func.combat as combat
import func.inventory as inventory
import func.chest as chest
import func.classes as classes

import random
import sys

meny = classes.user_input("1.Start game\n2.Exit",["1","2"])
if meny == 2:
    print("Exiting game...")
    sys.exit()
elif meny == 1:
    print("Entering the dungeon...")   

print("intro")

name = user_input("Choose name... ")

print(name)

print("begin")

choice = user_input("1.Open door\n2.Inventory\n3.Exit game\n\n",["1","2","3"])

if choice == "1":
    csd
elif choice == "2":
    inventory()
elif choice == "3":
    end = input("Are you sure? Y/N ")
    lower = end.lower()
    if lower == "y":
        print("Exiting game...")
        sys.exit()
    elif lower == "n":
        print("Returning to game...")

    else:
        print("Invalid input")
else:
    print("Invalid input")

