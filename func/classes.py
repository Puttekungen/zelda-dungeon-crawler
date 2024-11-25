class Player:

    inventory = {
    "fist": 0,

}

    def __init__(self, strength, hp, lvl, gold): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.gold = gold
        self.name = ""
        self.inventory = {"fist": {"type":"weapon","strength":100}}
                
    

