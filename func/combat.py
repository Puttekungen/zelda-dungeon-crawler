import random
import func.classes as classes

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
        print(f"{player.name} won, {player.name} found {gold} gold in the monster remains") 
        player.gold += gold
        player.lvl += 1
        print(f"{player.name} level up, +1 lvl")
        resume = input("press 'enter' to continue\n")
    elif player.strength == enemy_strength:
        print("Your fight ended in a tie")
        resume = input("press 'enter' to continue\n")
    # elif player.strength < enemy_strength:
    #     if # använda potion

    #     print(f"The monster won, {player.name} took {enemy_strength} damage")
    #     player.hp -= enemy_strength
    