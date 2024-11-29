
import func.inventory as inventory
import func.classes as classes
import random



class Shop:
    def __init__(self):
        small = random.randint(1, 2)
        elixir = random.randint(3, 5)
        sword = random.randint(5, 9)
        health = random.randint(3, 6)
        self.items = [
            classes.Item("Small Potion", "potion", small, 5),
            classes.Item("Strength Elixir", "potion", elixir, 10),
            classes.Item("Health Potion", "potion", health, 10),
            classes.Item("Iron Sword", "weapon", sword, 20),
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
                        
                        
                        if item.name == "Strength Elixir" or "Small Potion":
                            player.strength += item.strength_bonus
                            print(f"{player.name}'s strength increased by {item.strength_bonus}!")
                        else:
                            
                            player.add_item(item)
                    else:
                        print("You don't have enough gold!\n")
                        input("press 'enter' to continue")

                elif choice == 5:
                    print("Exiting the shop...\n")
                    break
                else:
                    print("Invalid choice. Try again.\n")
            else:
                print("Invalid input. Please enter a number.\n")
