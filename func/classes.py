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
        self.inventory = [{"fist":10}]
    