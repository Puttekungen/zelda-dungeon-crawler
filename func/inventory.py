def print_inventory(player):
    if player.inventory:
        print(f"{player.name}s Inventory:")
        for item in player.inventory:
            print(f"{player.inventory.index(item.name)}.{item.name}")
    
    else:
        print("Your inventory is empty.")
    input("press 'enter' to continue\n")

def use_potion(player): 
    
     
def add_to_inventory(player, item):
    if len(player.inventory) <= 5:
        player.inventory.append(item)
        print(f"You obtained: {item}\n")
    else:
        print("Your inventory is full! You can't carry more items.\n")
    input("press 'enter' to continue\n")
            

def total_strength(player):
        return player.strength + sum(item.strength_bonus for item in player.inventory)
