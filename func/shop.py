
import func.inventory as inventory
import random  

class Item:
    def __init__(self, name, strength_bonus, price):
        self.name = name
        self.strength_bonus = strength_bonus
        self.price = price

    def __str__(self):
        return f"{self.name} (STR Bonus: {self.strength_bonus}, Price: {self.price} Gold)"

class Shop:
    def __init__(self):
        self.items = [
            Item("Small Potion", 0, 5),
            Item("Strength Elixir", 3, 10),
            Item("Iron Sword", 5, 20),
            Item("Golden Shield", 4, 15),
        ]

    def display_items(self):
        print("\nShop Inventory:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")
        print("5. Exit Shop\n")

    def buy_item(self, player):
        while True:
            self.display_items()
            choice = input("Choose an item to buy (1-5): ").strip()


            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.items):
                    item = self.items[choice - 1]
                    if player.gold >= item.price:
                        player.gold -= item.price
                        player.add_item(item)
                    else:
                        print("You don't have enough gold!\n")
                elif choice == 5:
                    print("Exiting the shop...\n")
                    break
                else:
                    print("Invalid choice. Try again.\n")
            else:
                print("Invalid input. Please enter a number.\n")
