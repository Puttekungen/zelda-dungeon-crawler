import func.classes as classes

def level_up(player):
    print("Stats increased!")
    print(f"HP: {player.hp} --> {player.hp + 2}\nSTR: {player.strength} --> {player.strength + 2}\nLVL: {player.lvl} --> {player.lvl + 1}")
    player.lvl += 1
    player.strength += 2
    player.hp += 2
    