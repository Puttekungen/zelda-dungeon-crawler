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
else:
    print("Invalid input")


class Player:

    def __init__(self, namn, strength):
        self.name = name
        self.strength = strength

    def print_person_info(self):
        print(self.name)

print("intro")

name = input("Choose name...")

print(name)

print("begin")

c = choices("Open door","Inventory","Exit")

if c == 1:
    csd
elif c == 2:
    combat()
elif c == 3:
    print("Exiting game...")
    sys.exit()