import random

class Player:

    def __init__(self, strength, hp, lvl): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl


def combat(player):
    if player.lvl <= 9:
        enemy_strength = random.randint(9,14)
    elif player.lvl <= 6:
        enemy_strength = random.randint(7,10)
    elif player.lvl <= 3:
        enemy_strength = random.randint(5,8)
   
    
    damage = random.randint(2, 4)

   

    if player.strength > enemy_strength:
        print(f"The monster won, you took {damage} damage")
        player.hp -= damage
    elif player.strength < enemy_strength:
        print("nah") 
    elif player.strength == enemy_strength:
        print("monster won")
    
player = Player(10, 10, 2)
combat(player)

print(player.hp)
