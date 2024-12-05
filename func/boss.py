import sys
import random
import func.classes as classes

def boss(player):
    i = 0
    boss_choice = random.choices(["rat_king", "skeleton", "god"], [0.4,0.4,0.1], k=1)
    boss_choice = str(boss_choice[0])


    if boss_choice == "rat_king":
        boss_strength = random.randint(54,68)
        
        print(f"When {player.name} opens the door he spots a ladder going down and decides to climb it")
        input("press 'enter' to continue\n")
        
        print(f"{player.name} notices that he has entered some kind of sewer")
        input("press 'enter' to continue\n")
        
        print("The tunnel leads into a large dark room")
        input("press 'enter' to continue\n")
        
        print("Suddenly torches around the room light up and in the middle of the room a large creature appears")
        input("press 'enter' to continue\n")
        
        print("It's the RAT KING")
        input("press 'enter' to continue\n")
        
        print(f"The Rat king's strength is {boss_strength}")
        print("You start becoming a little nervous but steel your nerves and go to attack the monster")
        input("press 'enter' to continue")
            
        while True:
            if player.strength < boss_strength:
                print("You put everything you had into this final battle but weren't strong enough to end it")
                i += 1
                player.hp -= player.hp
                input("press 'enter' to continue\n")
                break
            elif player.strength == boss_strength:
                print(f"{player.name} and the Rat King have the same strength")
                input("press 'enter' to continue\n")
                print(f"{player.name} flips a coin to help him win")
                chance_time = random.choice(["Heads", "Tails"]).lower()
                choice = input("Choose:\n Heads or Tails\n").lower()
                
                if choice == "heads" or choice == "tails":
                    if chance_time == choice:
                        print("You guessed right")
                        print(f"{player.name} gains 1 str")
                        player.strength += 1
                        continue
                    elif chance_time != choice:
                        print("You got it wrong")
                        print("God gained 1 str")
                        boss_strength += 1
                        continue
                else:
                    print("Invalid input")
                    continue

            elif player.strength > boss_strength:
                print("The dungeon has made you strong enough to make kings fall")
                input("press 'enter' to continue\n")
                
                print("At the back of the room there is a door with a staircase leading up")
                input("press 'enter' to continue\n")
                
                print("At the top you find yourself finally outside and free from the horrors that the dungeon had to offer")
                input("press 'enter' to continue\n")
                
                print("GAME COMPLETED!")
                print("Exiting game...")
                sys.exit()


    elif boss_choice == "skeleton":
        boss_strength = random.randint(54,75)

        print("On the other side of the door you find a long pathway that leads to a giant door")
        input("press 'enter' to continue\n")
            
        print(f"{player.name} decides to open the door")
        input("press 'enter' to continue\n")
        
        print("On the other side of the giant door is a large room with a big pile of bones")
        input("press 'enter' to continue\n")
        
        print(f"{player.name} walks toward the pile to investigate")
        input("press 'enter' to continue\n")

        print("The pile of bones start shaking and then they slowly connect with each other in order to form a giant skeleton")
        input("press 'enter' to continue\n")

        print("The GIANT SKELETON has appeared")
        input("press 'enter' to continue\n")
        
        
        while True:
            if player.strength < boss_strength:
                print("You put everything you had into this final battle but weren't strong enough to end it")
                i += 1
                player.hp -= player.hp
                input("press 'enter' to continue\n")
                break
            elif player.strength == boss_strength:
                print(f"{player.name} and the Giant Skeleton have the same strength")
                input("press 'enter' to continue\n")
                print(f"{player.name} flips a coin to help him win")
                chance_time = random.choice(["Heads", "Tails"]).lower()
                choice = input("Choose:\n Heads or Tails\n").lower()
                
                if choice == "heads" or choice == "tails":
                    if chance_time == choice:
                        print("You guessed right")
                        print(f"{player.name} gains 1 STR")
                        player.strength += 1
                        continue
                    elif chance_time != choice:
                        print("You got it wrong")
                        print("The giant skeleton gained 1 STR")
                        boss_strength += 1
                        continue
                else:
                    print("Invalid input")
                    continue
                    

            elif player.strength > boss_strength:
                print("The dungeon has made you strong enough to make giants fall")
                input("press 'enter' to continue\n")
                print("At the back of the room there is a door with a staircase leading up")
                input("press 'enter' to continue\n")
                print("At the top you find yourself finally outside and free from the horrors that the dungeon had to offer")
                input("press 'enter' to continue\n")
                print("GAME COMPLETED!")
                print("Exiting game...")
                sys.exit()

    elif boss_choice == "god":
        boss_strength = random.randint(70,90)

        print(f"As {player.name} opens the door a increasingly bright light starts to peak through the door crack")
        input("press 'enter to continue\n")

        print(f"On the other side is a long pathway high above the clouds")
        input("press 'enter to continue\n")
        
        print(f"{player.name} walks along the path for what seems like forever but he finally reaches the end")
        input("press 'enter to continue\n")

        print(f"{player.name} spots a large figure sitting on an enormous chair")
        input("press 'enter to continue\n")
        
        print("The large figure stands up and presents you with a choice")
        input("press 'enter to continue\n")

        while i < 2:        
            defeat_or_attack = input("'Lay down in defeat and die or will you continue to defy my will tiny human?': [Defeat/Attack]\n").lower()

            if defeat_or_attack == "defeat":
                print("The large figure accepts your choice and drains your life energy")
                player.hp -= player.hp
                print(f"HP: {player.hp}")
                input("Press 'enter' to continue\n")
                break
            
            elif defeat_or_attack == "attack":
                print("'Very well, I will allow you to humor me human'")
                input("press 'enter to continue\n")

                print("'But first you must know who I am'")
                input("press 'enter to continue\n")

                print("'I am the god that governs the world that you live in'")
                yes_no = input("'Knowing that do you still wish to continue?': [Y/n]").lower()

                while i < 1:
                    if yes_no == "y" or yes_no == "":
                        print("'Okay, you have made your choice, there's no going back now'")
                        input("press 'enter to continue\n")

                        print(f"Opponent: 'GOD'\n Strength: {boss_strength}")
                        input("press 'enter to continue\n")

                        while True:
                            if player.strength < boss_strength:
                                print("You put everything you had into this final battle but weren't strong enough to end it")
                                i += 1
                                player.hp -= player.hp
                                input("press 'enter' to continue\n")
                                break
                            elif player.strength == boss_strength:
                                print(f"{player.name} and God have the same strength")
                                input("press 'enter' to continue\n")
                                print(f"{player.name} flips a coin to help him win")
                                chance_time = random.choice(["Heads", "Tails"]).lower()
                                choice = input("Choose:\n Heads or Tails\n").lower()
                            
                                if choice == "heads" or choice == "tails":
                                    if chance_time == choice:
                                        print("You guessed right")
                                        print(f"{player.name} gains 1 str")
                                        player.strength += 1
                                        continue
                                    elif chance_time != choice:
                                        print("You got it wrong")
                                        print("God gained 1 str")
                                        boss_strength += 1
                                        continue
                                else:
                                    print("Invalid input")
                                    continue
                                    

                            elif player.strength > boss_strength:
                                print("The dungeon has made you strong enough to make gods fall")
                                input("press 'enter' to continue\n")
                                print("Your surroundings start to become blurry and they eventually turn back into the dungeon that you were just in")
                                input("press 'enter' to continue\n")
                                print("At the back of the room there is a door with a staircase leading up")
                                input("press 'enter' to continue\n")
                                print("At the top you find yourself finally outside and free from the horrors that the dungeon had to offer")
                                input("press 'enter' to continue\n")
                                print("GAME COMPLETED!")
                                print("Exiting game...")
                                sys.exit()

                    elif yes_no == "n":
                        break
                i += 1
            
            else:
                print("Invalid input")
                continue