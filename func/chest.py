from classes import Player
import random

player = Player(10, 20, 9, 4)
Sword = 5
name = "ooga"

def mimic(player):
    if player.lvl >= 9:
        mimic_str = random.randint(9,14)
        gold = random.randint(2,6)
    elif player.lvl >= 6:
        mimic_str = random.randint(7,10)
        gold = random.randint(2,3)
    elif player.lvl >= 3:
        mimic_str = random.randint(5,8)
        gold = random.randint(1,3)
    else:
        mimic_str = random.randint(2,4)
        gold = random.randint(1,2)
          
          
    if player.strength < mimic_str:
        print(f"The mimic won, {name} took {mimic_str} damage")
        player.hp -= mimic_str
    elif player.strength > mimic_str:
        print(f"{name} won, {name} found {gold} gold inside the defeated mimic") 
        player.gold += gold
    elif player.strength == mimic_str:
        print("Your fight ended in a tie")
    

def chest():
    global Sword

    item_num = random.randint(1,5)
    if item_num >= 4: 
        str = random.randint(3,5)
        print(f"{name} found a +{str} strength potion")
    elif item_num >= 2:
        health = ("Health Potion")
    elif item_num >= 1:
        if player.lvl >= 9:
            power = random.randint(9,14)
        elif player.lvl >= 6:
            power = random.randint(7,10)
        elif player.lvl >= 3:
            power = random.randint(5,8)
        else:
            power = random.randint(2,4)

        Sword += power

        print(f"Sword power {Sword}")
 

def type():
    typ = random.randint(1,5)
    
    if typ >= 3:
        mimic(player)
    elif typ < 3:
        chest()

type()
print(player.hp)
print(player.lvl)