import random

class Item:
    def __init__(self, name, type, strength_bonus=0, price=0, health_bonus=0):
        self.name = name
        self.type = type
        self.strength_bonus = strength_bonus
        self.price = price
        self.health_bonus = health_bonus

    def __str__(self):
        return f"{self.name} (STR Bonus: {self.strength_bonus}, Price: {self.price} Gold)"

class Player:

    def __init__(self, strength, hp, lvl, gold, name): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.gold = gold
        self.name = name
        self.inventory = []
        self.current_weapon = None

class Enemy:

    def __init__(self, lvl):
        names=["zombie","skeleton","ghost","goblin","spider","phantom"]
        if lvl >= 8:
            self.strength = random.randint(30,40)
            self.gold = random.randint(8,15)
        elif lvl >= 5:
            self.strength = random.randint(29,37)
            self.gold = random.randint(5,9)
        elif lvl >= 3:
            self.strength = random.randint(15,29)
            self.gold = random.randint(2,4)
        else:
            self.strength = random.randint(9,15)
            self.gold = random.randint(1,3)
        self.name = random.choice(names)

