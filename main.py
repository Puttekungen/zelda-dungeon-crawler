from func.trap import traps, trap
from func.shop import Shop
from func.combat import *
from func.inventory import *
from func.chest import *
import func.classes

import random
import sys
<<<<<<< HEAD
from func.classes import *
=======
>>>>>>> 1df6e6bc9aff7dcc0d7cb2fb8fdeeb4d61d22920

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

