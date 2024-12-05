import func.classes as classes

def level_up(player): # Visar hur statsen ökar när använder går upp i lvl
    print("Stats increased!")
    print(f"HP: {player.hp} --> {player.hp + 3}\nSTR: {player.strength} --> {player.strength + 3}\nLVL: {player.lvl} --> {player.lvl + 1}")
    player.lvl += 1
    player.strength += 3
    player.hp += 3
    