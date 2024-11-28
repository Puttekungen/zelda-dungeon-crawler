import random

class Player:

    available_items = {
        "fist": {
            "type": "weapon",
            "strength": 100
        },
        "sword": {
        "type": "weapon",
        "strength": 100
        },
        "sword": {
        "type": "weapon",
        "strength": 100
        },
    }

    def __init__(self, strength, hp, lvl, gold, name): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.gold = gold
        self.name = name
        self.inventory = {"fist": {"type":"weapon","strength":100}}

    inventory = {
        "fist": {
            "type": "weapon",
            "strength": 100
        },
    }

class Enemy:
    names=["Zombie","Skeleton"]


    def __init__(self, lvl):
        if lvl >= 8:
            self.strength = random.randint(9,14)
            self.gold = random.randint(2,6)
        elif lvl >= 5:
            self.strength = random.randint(7,10)
            gold = random.randint(2,3)
        elif lvl >= 3:
            self.strength = random.randint(5,8)
            self.gold = random.randint(1,3)
        else:
            self.strength = random.randint(2,4)
            self.gold = random.randint(1,2)
