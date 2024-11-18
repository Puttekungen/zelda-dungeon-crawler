lista = []
from allt import *
import random
import sys

def choices(c):
    while True:
        for i in range(len(c)):
                print(f"{i+1}.{c[i]}")
        choice=input("\n")
        for i in range(len(c)):
            if str(i+1)==choice:
                return int(choice)


meny = choices(["Start game","Exit"])
if meny == 2:
    print("Exiting game...")
    sys.exit()
elif meny == 1:
    print("Entering the dungeon...")   



class Player:

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def print_person_info(self):
        print(self.name)

print("intro")

name = input("Choose name... ")

print(name)

print("begin")

c = input("1.Open door\n2.Inventory\n3.Exit game\n\n")

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
