import random
import func.classes as classes

def boss(player):
    which = random.randint(1,3)

    if which == 1:
        print(f"When {player.name} opens the door he spots a ladder going down and decides to climb it")
        resume = input("press 'enter' to continue\n")
        print(f"{player.name} notices that he has entered somekind of sewer")
        resume = input("press 'enter' to continue\n")

        # rat_king

    # elif which == 2:
    #     Giant Skeleton

    # elif which == 3:
    #     God