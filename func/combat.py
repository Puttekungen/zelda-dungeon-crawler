import random
import func.classes as classes
from func.levelup import level_up

def combat(player):
    enemy = classes.Enemy(player.lvl)

    situations = ["jumps in front of you","walks towards you","peeks out behind a corner","appears"]

    input(f"A {enemy.name} {random.choice(situations)}\n")

    if player.strength > enemy.strength:
        print(f"{player.name} won, {player.name} found {enemy.gold} gold in the monster remains") 
        player.gold += enemy.gold
        level_up(player)
        print(f"{player.name} level up, +1 lvl")
        print(f"Current lvl: {player.lvl}\n")
        print("Stats increased")
        input("press 'enter' to continue\n")

    elif player.strength == enemy.strength:
        print("Your fight ended in a tie")
        input("press 'enter' to continue\n")

    elif player.strength < enemy.strength:
        print(f"The monster won, {player.name} took {enemy.strength} damage")
        player.hp -= enemy.strength
        input("press 'enter' to continue\n")
    
