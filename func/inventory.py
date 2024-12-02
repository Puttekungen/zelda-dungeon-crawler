def get_user_input(text, valid_input):
    while True:
        user_input=input(f"{text}")
            
        for i in range(len(valid_input)):
            if str(valid_input[i]).lower() == user_input:
                return user_input
        print("Invalid input")

def print_inventory(player):
    print(f"{player.name}s Inventory:")
    for i, item in enumerate(player.inventory, start=1):
        print(f"{i}. {item.name}")

def inventory(player):
    if player.inventory:
        print_inventory(player)
        slots = [i + 1 for i in range(len(player.inventory))]
        decide = get_user_input("Choose what to inspect: ", slots)

        if decide != "":
            item = player.inventory[int(decide) - 1]

            # Visa attribut för health potions
            print(f"{item.name}: Healing: {item.health_bonus}\n")
            decide = input("Do you want to use this potion? [y/N]: ")
            if decide.lower() == "y":
                use_potion(player, item)
            elif decide.lower() == "n" or decide == "":
                print("Item not used")
            
    else:
        print("Your inventory is empty.")
    
    input("\nPress 'enter' to continue\n")



def use_potion(player, item):
    if item.health_bonus > 0:
        player.hp += item.health_bonus
        player.inventory.remove(item)
        print(f"You used {item.name} and restored {item.health_bonus} HP")
        print(f"Current HP: {player.hp}\n")
    else:
        print("This item cannot be used as a potion.\n")
     
def add_to_inventory(player, item):
    if len(player.inventory) <= 5:
        player.inventory.append(item)
        print(f"You obtained: {item}\n")
        input("\nPress 'enter' to continue\n")
    else:
        print("Your inventory is full! You can't carry more items.\n")

        while True:
            decide = input(f"\nDo you want to replace a slot? [Y/n] ")
            if decide.lower() == "y":
                print_inventory()
                slots = []
                for i in range(len(player.inventory)):
                    slots.append(i+1)
                decide = get_user_input("Choose what to replace: ", slots)
                player.inventory[int(decide)] = item
                input("press 'enter' to continue\n")
                break

            elif decide.lower() == "n":
                break

            else:
                print("Invalid input")
            

def total_strength(player):
        return player.strength + sum(item.strength_bonus for item in player.inventory)
