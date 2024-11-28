import random
import func.classes as classes

def boss(player):
    which = random.randint(1,3)
    test = random.choices(["rat_king", "skeleton", "god"], [0.4,0.4,0.1], k=1)
    test = str(test[0])

    print(test)
    if test == "rat_king":
        print(f"When {player.name} opens the door he spots a ladder going down and decides to climb it")
        resume = input("press 'enter' to continue\n")
        print(f"{player.name} notices that he has entered somekind of sewer")
        resume = input("press 'enter' to continue\n")

        # rat_king

    # elif which == 2:
    #     Giant Skeleton

    # elif which == 3:
    #     God