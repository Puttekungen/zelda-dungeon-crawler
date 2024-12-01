import func.classes as classes
import random

def mimic(player):
    if player.lvl >= 8:
        mimic_str = random.randint(9,14)
        gold = random.randint(2,6)
    elif player.lvl >= 5:
        mimic_str = random.randint(7,10)
        gold = random.randint(2,3)
    elif player.lvl >= 3:
        mimic_str = random.randint(5,8)
        gold = random.randint(1,3)
    else:
        mimic_str = random.randint(2,4)
        gold = random.randint(1,2)
          
    print("The chest turns out to be a mimic")      
    if player.strength < mimic_str:
        print(f"The mimic won, {player.name} took {mimic_str} damage")
        player.hp -= mimic_str
        resume = input("press 'enter' to continue\n")
    elif player.strength > mimic_str:
        print(f"{player.name} won, {player.name} found {gold} gold inside the defeated mimic") 
        player.gold += gold
        player.lvl += 1
        print(f"{player.name} leveled up, +1 lvl")
        print(f"Current lvl: {player.lvl}\n")
        resume = input("press 'enter' to continue\n")
    elif player.strength == mimic_str:
        print("Your fight ended in a tie")
        resume = input("press 'enter' to continue\n")
    

def chest(player):
    item_num = random.randint(1,5)
    if item_num >= 4: 
        strength = random.randint(3,5)
        player.strength += strength
        print(f"Inside, {player.name} finds a +{strength} strength potion")
        print(f"{player.name}s total strength is now {player.strength}!\n")
    elif item_num >= 2:
        health = random.randint(3,5)
        health_potion = classes.Item("Health Potion", "potion", health_bonus=health)
        if len(player.inventory) <= 10:
            player.inventory.append(health_potion)
            print(f"{player.name} found a +{health} health potion")
        else:
            print("Your inventory is full! You can't carry more items.\n")

    elif item_num >= 1:
        if player.lvl >= 8:
            power = random.randint(9,14)
            print(power)
        elif player.lvl >= 5:
            power = random.randint(7,10)
        elif player.lvl >= 3:
            power = random.randint(5,8)
        else:
            power = random.randint(2,4)
 

def type(player):
    typ = random.randint(1,5)
    print(f"{player.name} finds a chest")
    input("press 'enter' to continue\n")
    
    if typ >= 3:
        mimic(player)
    elif typ < 3:
        chest(player)

