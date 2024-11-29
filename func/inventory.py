def get_user_input(text, valid_input):
    while True:
        user_input=input(f"{text}")
            
        for i in range(len(valid_input)):
            if str(valid_input[i]).lower() == user_input:
                return user_input
        print("Invalid input")

def inventory(player):
    if player.inventory:
        print_inventory(player)
    else:
        print("Your inventory is empty.")
    input("press 'enter' to continue\n")

def print_inventory(player):
    print(f"{player.name}s Inventory:")
    for item in player.inventory:
        print(f"{player.inventory.index(item.name)}.{item.name}")

def use_potion(player, item): 
    player.inenvtory
     
def add_to_inventory(player, item):
    if len(player.inventory) <= 5:
        player.inventory.append(item)
        print(f"You obtained: {item}\n")
    else:
        print("Your inventory is full! You can't carry more items.\n")

        while True:
            decide = input(f"Do you want to replace a slot? [Y/n] ")
            if decide.lower() == "y":
                print_inventory()
                slots = []
                for i in len(player.inventory):
                    slots.append(i)
                decide = get_user_input("Choose what to replace: ", slots)
                player.inventory[int(decide)-1] = item
                input("press 'enter' to continue\n")
                break
            elif decide.lower() == "n":
                break

            else:
                print("Invalid input")
            

def total_strength(player):
        return player.strength + sum(item.strength_bonus for item in player.inventory)
