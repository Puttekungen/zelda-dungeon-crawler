import random
import func.classes as classes

def boss(player):
    which = random.randint(1,3)
    boss_choice = random.choices(["rat_king", "skeleton", "god"], [0.4,0.4,0.1], k=1)
    boss_choice = str(boss_choice[0])

    print(boss_choice)
    if boss_choice == "rat_king":
        print(f"When {player.name} opens the door he spots a ladder going down and decides to climb it")
        resume = input("press 'enter' to continue\n")
        print(f"{player.name} notices that he has entered some kind of sewer")
        resume = input("press 'enter' to continue\n")
        print("The tunnel leads into a large dark room")
        resume = input("press 'enter' to continue\n")
        print("Suddenly torches around the room light up and in the middle of the room a large creature appears")
        resume = input("press 'enter' to continue")
        print("It's the RAT KING")
        

    if boss_choice == "skeleton":
        print("Giant skeleton")

    elif boss_choice == "god":
        print("god")