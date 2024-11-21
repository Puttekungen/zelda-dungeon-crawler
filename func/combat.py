import random
from classes import Player


def combat(player):
    if player.lvl >= 9:
        enemy_strength = random.randint(9,14)
        gold = random.randint(2,6)
    elif player.lvl >= 6:
        enemy_strength = random.randint(7,10)
        gold = random.randint(2,3)
    elif player.lvl >= 3:
        enemy_strength = random.randint(5,8)
        gold = random.randint(1,3)
    else:
        enemy_strength = random.randint(2,4)
        gold = random.randint(1,2)
   


    if player.strength < enemy_strength:
        print(f"The monster won, you took {enemy_strength} damage")
        player.hp -= enemy_strength
    elif player.strength > enemy_strength:
        print(f"You won, you found {gold} gold in the monster remains") 
        player.gold += gold
    elif player.strength == enemy_strength:
        print("Your fight ended in a tie")
    
player = Player(10, 20, 9, 4)
combat(player)

print(player.hp)
print(player.gold)
