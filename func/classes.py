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

class Monster:
    all_monsters = {
    "fist": {
        "hp": 100,
        "strength": 100
    },
}
