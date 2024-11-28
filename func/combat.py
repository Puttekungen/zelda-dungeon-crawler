import random
from func.classes import *

def combat(player):
    enemy = Enemy(player.lvl)

    if player.strength > enemy.strength:
        print(f"{player.name} won, {player.name} found {enemy.gold} gold in the monster remains") 
        player.gold += enemy.gold
        player.lvl += 1
        print(f"{player.name} leveled up, +1 lvl")
        input("press 'enter' to continue\n")

    elif player.strength == enemy_strength:
        print("Your fight ended in a tie")
        input("press 'enter' to continue\n")

    elif player.strength < enemy_strength






# elif player.strength < enemy_strength:
    #     if # använda potion

    #     print(f"The monster won, {player.name} took {enemy_strength} damage")
    #     player.hp -= enemy_strength
    