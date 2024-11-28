<<<<<<< HEAD



inventory = []

inventory.append 
=======
def inventory(player):
# Loop through inventory and print each item with its type and strength
    print(f"{player.name}'s inventory:\n")
    for index, (item, properties) in enumerate(player.inventory.items(), start=1):
        item_type = properties["type"]
        item_strength = properties["strength"]
        print(f"{index}. {item}: Type: {item_type}, Strength: {item_strength}")
>>>>>>> 1037e440075214d95be810b1e307dc33400ec7b1
