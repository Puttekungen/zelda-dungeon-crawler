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
        slots = []
        for i in range(len(player.inventory)):
            slots.append(i+1)
        decide = get_user_input("Choose what to inspect: ", slots)
        item = player.inventory[int(decide)-1]

        if item.type=="potion":
            print(f"{item.name}: Healing: {item.healing}\n")
        else:
            print(f"{item.name}: Healing: {item.strength_bonus}\n")

    else:
        print("Your inventory is empty.")
    input("press 'enter' to continue\n")

def use_potion(player, item): 
    player.inventory
     
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
