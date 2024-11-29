def print_inventory(player):
        if player.inventory:
            print(f"{player.name}s Inventory:")
            for item in player.inventory:
                print(f"{player.inventory.index(item.name)}.{item.name}")
        else:
            print("Your inventory is empty.")
        print()

def use_item(player): 
     
     
def add_item(player, item):
        if len(player.inventory) <= 10:
            player.inventory.append(item)
            print(f"You obtained: {item}\n")
        else:
            print("Your inventory is full! You can't carry more items.\n")
def total_strength(player):
        return player.strength + sum(item.strength_bonus for item in player.inventory)
