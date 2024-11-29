import random
import func.classes as classes

def boss(player):
    which = random.randint(1,3)
    boss_choice = random.choices(["rat_king", "skeleton", "god"], [0.4,0.4,0.1], k=1)
    boss_choice = str(boss_choice[0])


    if boss_choice == "rat_king":
        boss_health = random.randint(30,50)
        print(f"When {player.name} opens the door he spots a ladder going down and decides to climb it")
        resume = input("press 'enter' to continue\n")
        print(f"{player.name} notices that he has entered some kind of sewer")
        resume = input("press 'enter' to continue\n")
        print("The tunnel leads into a large dark room")
        resume = input("press 'enter' to continue\n")
        print("Suddenly torches around the room light up and in the middle of the room a large creature appears")
        resume = input("press 'enter' to continue\n")
        print("It's the RAT KING")
        resume = input("press 'enter' to continue\n")
        print(f"The Rat king's strength is {boss_health}")
        print("You start becoming a little nervous but steel your nerves and go to attack the monster")
        resume = input("press 'enter' to continue")
        
        if player.strength < boss_health:
            print("You put everything you had into this final battle but weren't strong enough to end it")
            print("YOU DIED")
            resume = input("press 'enter' to continue\n")
        elif player.strength == boss_health:
            print(f"{player.name} and the Rat King have the same strength")
            resume = input("press 'enter' to continue\n")
            print(f"{player.name} flips a coin to help him win")
            chance_time = random.choice("Heads", "Tails")
            choice = input("Choose 1.Heads or 2.Tails")
            if chance_time == choice:
                print("You guessed right")
                print(f"{player.name} gains 1 str")
                player.strength += 1
                # ska göra så att när de har samma strength så ska den gå tillbaka till där den kollar om spelaren har mer eller mindre str för att kolla igen
            elif chance_time != choice:
                print("You got it wrong")
                print("The Rat King gained 1 str")
                boss_health += 1
        elif player.strength > boss_health:
            print("The dungeon has made you strong enough to make kings fall")
            resume = input("press 'enter' to continue\n")
            print("At the back of the room there is a door with a staircase leading up")
            resume = input("press 'enter' to continue\n")
            print("At the top you find yourself finally outside and free from the horrors that the dungeon had to offer")
            resume = input("press 'enter' to continue\n")
            print("GAME COMPLETED!")


    if boss_choice == "skeleton":
        print("Giant skeleton")

    elif boss_choice == "god":
        print("god")

