import func.classes as classes
from func.weapon import *
from func.levelup import *
import random

def mimic(player):
    if player.lvl >= 8:
        mimic_str = random.randint(30,40)
        gold = random.randint(8,15)
    elif player.lvl >= 5:
        mimic_str = random.randint(29,37)
        gold = random.randint(5,9)
    elif player.lvl >= 3:
        mimic_str = random.randint(15,29)
        gold = random.randint(2,4)
    else:
        mimic_str = random.randint(9,15)
        gold = random.randint(1,2)
          
    print("The chest turns out to be a mimic")      
    if player.strength < mimic_str:
        print(f"The mimic won, {player.name} took {mimic_str} damage")
        player.hp -= mimic_str
        input("press 'enter' to continue\n")
    elif player.strength > mimic_str:
        print(f"{player.name} won, {player.name} found {gold} gold inside the defeated mimic") 
        player.gold += gold
        level_up(player)
        input("press 'enter' to continue\n")
    elif player.strength == mimic_str:
        print("Your fight ended in a tie")
        input("press 'enter' to continue\n")
    

def chest(player):
    item_num = random.randint(1,5)
    if item_num >= 4: 
        strength = random.randint(3,6)
        player.strength += strength
        print(f"Inside, {player.name} finds a +{strength} strength potion")
        print(f"{player.name}s total strength is now {player.strength}!\n")
        input("press 'enter' to continue\n")
        
    elif item_num >= 2:
        health = random.randint(4,6)
        health_potion = classes.Item("Health Potion", "potion", health_bonus=health)
        if len(player.inventory) <= 5:
            player.inventory.append(health_potion)
            print(f"{player.name} found a +{health} health potion")
        else:
            print("Your inventory is full! You can't carry more items.\n")

    elif item_num >= 1:
        if player.lvl >= 8:
            power = random.randint(8,14)
            item = [classes.Item("Iron Sword", "weapon", strength_bonus=power, price=0)]
            weapon_pickup(player, item[0])
        elif player.lvl >= 5:
            power = random.randint(6,10)
            item = [classes.Item("Iron Sword", "weapon", strength_bonus=power, price=0)]
            weapon_pickup(player, item[0])
        elif player.lvl >= 3:
            power = random.randint(4,7)
            item = [classes.Item("Iron Sword", "weapon", strength_bonus=power, price=0)]
            weapon_pickup(player, item[0])
        else:
            power = random.randint(2,5)
            item = [classes.Item("Iron Sword", "weapon", strength_bonus=power, price=0)]
            weapon_pickup(player, item[0])

        print(f"{player.name} found a new weapon")
 


def type(player):
    typ = random.randint(1,4)
    print(f"{player.name} finds a chest")
    input("press 'enter' to continue\n")
    
    if typ >= 3:
        mimic(player)
    elif typ < 3:
        chest(player)

