import random
import func.classes as classes

def combat(player):
    enemy = classes.Enemy(player.lvl)

    situations = ["jumps in front of you","walks towards you","peeks out behind a corner","appears"]

    input(f"A {enemy.name} {random.choice(situations)}\n")

    if player.strength > enemy.strength:
        print(f"{player.name} won, {player.name} found {enemy.gold} gold in the monster remains") 
        player.gold += enemy.gold
        player.lvl += 1
        print(f"{player.name} level up, +1 lvl")
        input("press 'enter' to continue\n")

    elif player.strength == enemy.strength:
        print("Your fight ended in a tie")
        input("press 'enter' to continue\n")

    elif player.strength < enemy.strength:
        sure = input(f"{enemy.name} is stronger than you. Do you want to use a potion? [Y/n] ")
        while True:
            if sure.lower() == "y":
                print("Entering game...\n")
                return player
            elif sure.lower() == "n":
                break
            else:
                print("Invalid input")

        print(f"The monster won, {player.name} took {enemy.strength} damage")
        player.hp -= enemy.strength
        input("press 'enter' to continue\n")
    
