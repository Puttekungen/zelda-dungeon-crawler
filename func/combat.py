import random
from classes import *



def combat(player):
    if player.lvl >= 8:
        enemy_strength = random.randint(9,14)
        gold = random.randint(2,6)
    elif player.lvl >= 5:
        enemy_strength = random.randint(7,10)
        gold = random.randint(2,3)
    elif player.lvl >= 3:
        enemy_strength = random.randint(5,8)
        gold = random.randint(1,3)
    else:
        enemy_strength = random.randint(2,4)
        gold = random.randint(1,2)
   


    if player.strength > enemy_strength:
        print(f"You won, you found {gold} gold in the monster remains") 
        player.gold += gold
        player.lvl += 1
        print(f"{name} leveled up, +1 lvl")
        print("+1 lvl")
    elif player.strength == enemy_strength:
        print("Your fight ended in a tie")
    elif player.strength < enemy_strength:
        try: # använda potion

        print(f"The monster won, you took {enemy_strength} damage")
        player.hp -= enemy_strength
    
combat(player)

print(player.hp)
print(player.gold)
print(player.lvl)
