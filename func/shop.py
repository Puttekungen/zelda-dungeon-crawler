import random
class Shop:
    def __init__(self): 
        self.items = {
            "Strenght potion" : 10,
            "Healing potion" : 10,
            "Weapon" : 25,
        }
budget = 100 

def display_items(self):
    print("\n---Welcomme to the shop ---")
    print("Here is what you can choose from:")
    for item, price in self.items():
         print(f"{item}: {price} $")
         print(f"\nYour budget: {budget} $")
        
def buy_item(self, choice):
    if choice in self.items:
        price =     self.items[choice]

        if budget >= price:
            print(f"You bought {choice} for {price} $!")
            print(f"You feel that your money bag got lighter,you got this much left: {budget}")

    else:
        print("You dont have enough money!")

    else: 
        print("") 

