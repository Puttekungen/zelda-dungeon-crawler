def equip_weapon(player, item):
        if player.current_weapon:
            player.strength -= player.current_weapon.strength_bonus

        player.current_weapon = item
        player.strength += item.strength_bonus
        print(f"Equipped {item.name} +{item.strength_bonus} STR")
        input("press 'enter' to continue\n")

        
def weapon_pickup(player, item):
    if player.current_weapon:
        while True:
            choice = input(f"Do you want to replace your current weapon {player.current_weapon.name} +{player.current_weapon.strength_bonus}STR with {item.name} +{item.strength_bonus}STR? [Y/n]\n").lower()
            if choice == "y" or choice == "":
                equip_weapon(player, item)
                break
            elif choice == "n":
                print(f"{player.name} threw away {item.name}")
                break
            else:
                print("Invalid input")
    else:
        equip_weapon(player, item)