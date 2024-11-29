import random
import func.classes as classes

def boss(player):
    while True:
        boss_choice = random.choices(["rat_king", "skeleton", "god"], [0.4,0.4,0.1], k=1)
        boss_choice = str(boss_choice[0])


        if boss_choice == "rat_king":
            boss_strength = random.randint(10,10)
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
            
            if player.strength < boss_strength:
                print("You put everything you had into this final battle but weren't strong enough to end it")
                print("YOU DIED")
                input("press 'enter' to continue\n")
                break
            elif player.strength == boss_strength:
                print(f"{player.name} and the Rat King have the same strength")
                input("press 'enter' to continue\n")
                print(f"{player.name} flips a coin to help him win")
                chance_time = random.choice(["Heads", "Tails"]).lower()
                choice = input("Choose:\n 1.Heads or 2.Tails\n").lower()
                if choice == "1":
                    choice = "Heads"
                elif choice == "2":
                    choice = "Tails"
                else:
                    print("Invalid choice, please choose 1 or 2.")
                    continue 
                
                if chance_time == choice:
                    print("You guessed right")
                    print(f"{player.name} gains 1 str")
                    player.strength += 1
                elif chance_time != choice:
                    print("You got it wrong")
                    print("The Rat King gained 1 str")
                    boss_strength += 1
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


        if boss_choice == "skeleton":
            print("Giant skeleton")

        elif boss_choice == "god":
            print("god")

