
import random  

class Shop:  # Definierar en klass som heter shop
    def __init__(self):  
        self.items = {  
            "strength potion": 10,
            "healing potion": 10,
            "weapon": 25,
        }
        self.budget = 100 
    def display_items(self):  # Visar tillgängliga föremål i shopen
        print("\n--- Welcome to the shop ---")  
        print("Here is what you can choose from:")  
        for item, price in self.items.items():  #  genom föremål och priser i ordboken
            print(f"{item.title()}: {price} $")  # Skriver ut varje föremål med pris
        print(f"\nYour budget: {self.budget} $")  

    def buy_item(self, choice):  # Metod som hanterar köp av ett föremål
        choice = choice.lower()  # Denna gör så att det inte spelar roll om man skriver i low caps
        if choice in self.items:  # Kollar om föremålet finns i shopen
            price = self.items[choice]  # Hämtar priset för det valda föremålet
            if self.budget >= price:  # Kontrollera om användaren har tillräckligt med pengar
                self.budget -= price  # Minskar budgeten med föremålets pris
                print(f"You bought {choice.title()} for {price} $!")  # Bekräftar köpet
                print(f"Your bag feels lighter, you have {self.budget} $ left.")  # Visar ny budget
            else:  # Om användaren inte har råd med föremålet
                print(f"You don't have enough money to buy {choice.title()}!")  
                print(f"It costs {price} $, but you only have {self.budget} $.")  
        else:  
            print(f"'{choice.title()}' is not available in the shop. Please choose a valid item.")  # Felmeddelande

def main():  
    shop = Shop()  # Skapar ett Shop-objekt
    while True:  # Startar en evig loop för att hålla shoppen aktiv
        shop.display_items()  # Visar föremål och budget
        choice = input("\nWhat would you like to buy? (type 'exit' to leave): ").strip()  

        if not choice:  # Kontrollera om användaren inte skrev något
            print("You didn't enter anything! Please type the name of an item or 'exit'.")  
            continue  # Gå tillbaka till början av loopen

        if choice.lower() == "exit":  # Kontrollera om användaren vill avsluta
            print("Thanks for visiting the shop!") 
            break  
        
        shop.buy_item(choice)  # Försök att köpa det valda föremålet


if __name__ ==  "__main__":
    main()