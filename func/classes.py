import random

class Item: # items namn hur mycket de kostar och hur mycket str/health de ger
    def __init__(self, name, type, strength_bonus=0, price=0, health_bonus=0):
        self.name = name
        self.type = type
        self.strength_bonus = strength_bonus
        self.price = price
        self.health_bonus = health_bonus

    def __str__(self):
        return f"{self.name} (STR Bonus: {self.strength_bonus}, Price: {self.price} Gold)"

class Player: # användarens stats

    def __init__(self, strength, hp, lvl, gold, name): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.gold = gold
        self.name = name
        self.inventory = []
        self.current_weapon = None

class Enemy: # de olika fienderna som kan attackera och deras styrka och hur mycket guld de kan ge

    def __init__(self, lvl):
        names=["zombie","skeleton","ghost","goblin","spider","phantom"]
        if lvl >= 8:
            self.strength = random.randint(35,45)
            self.gold = random.randint(12,18)
        elif lvl >= 5:
            self.strength = random.randint(25,35)
            self.gold = random.randint(8,12)
        elif lvl >= 3:
            self.strength = random.randint(15,25)
            self.gold = random.randint(4,6)
        else:
            self.strength = random.randint(10,15)
            self.gold = random.randint(2,4)
        self.name = random.choice(names)

