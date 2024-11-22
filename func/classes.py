class Player:

    def __init__(self, strength, hp, lvl, gold): 
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.gold = gold
        self.name = ""




def user_input(text, valid_input=None):
    while True:

        user_text=input(f"{text}\n")

        if user_text != "":
            if valid_input is None:
                return user_text
            
            for i in range(len(valid_input)):
                if valid_input[i].lower()==user_text:
                    return user_text