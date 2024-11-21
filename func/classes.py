class Player:

    def __init__(self, strength, hp, lvl, gold): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.gold = gold
        self.name = ""




def user_input(src, valid_input=None):
    while True:
        text=input(f"{src}\n")
        if text != "":
            if valid_input is None:
                return text
            for i in range(len(valid_input)):
                if valid_input[i].lower()==text:
                    return text
        print(f"Enter a valid input.\n")
