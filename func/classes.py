import random

class Item:
    def __init__(self, name, type, strength_bonus, price, healing=None):
        self.name = name
        self.type = type
        self.strength_bonus = strength_bonus
        self.price = price
        if self.type=="potion":
            self.healing = healing

    def __str__(self):
        return f"{self.name} (STR Bonus: {self.strength_bonus}, Price: {self.price} Gold)"

class Player:

    def __init__(self, strength, hp, lvl, gold, name): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.gold = gold
        self.name = name
        self.inventory = [Item("Empty", "none", 0, 0)]
        self.current_weapon = None

class Enemy:

    def __init__(self, lvl):
        names=["zombie","skeleton","ghost","goblin","spider","orc","phantom"]
        if lvl >= 8:
            self.strength = random.randint(9,14)
            self.gold = random.randint(2,6)
        elif lvl >= 5:
            self.strength = random.randint(7,10)
            self.gold = random.randint(2,3)
        elif lvl >= 3:
            self.strength = random.randint(5,8)
            self.gold = random.randint(1,3)
        else:
            self.strength = random.randint(2,4)
            self.gold = random.randint(1,2)
        self.name = random.choice(names)

