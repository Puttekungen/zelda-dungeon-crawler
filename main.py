from func.trap import traps, trap
from func.shop import Shop
from func.combat import *
from func.inventory import *
from func.chest import *
import func.classes

import random
import sys

meny = ("1.Start game\n2.Exit",["1","2"])
if meny == 2:
    print("Exiting game...")
    sys.exit()
elif meny == 1:
    print("Entering the dungeon...")   

print("intro")

name = user_input("Choose name... ")

print(name)

print("begin")

c = user_input("1.Open door\n2.Inventory\n3.Exit game\n\n",["1","2","3"])

if c == "1":
    csd
elif c == "2":
    inventory()
elif c == "3":
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

