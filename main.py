lista = []
from allt import *
import random
import sys

print("1.Start game")
print("2.Exit")
meny = input("")
if meny == "2":
    print("Nu avslutas programmet...")
    sys.exit()
elif meny == "1":
    print("Entering the dungeon...")   
    trap()
else:
    print("Ogiltig inmatning")

