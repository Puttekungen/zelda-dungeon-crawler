import random as rand

traps = ["You got shot by a hidden crossbow and took ", "You step on a hidden pressure plate and a metal chest falls from the ceiling hitting you in the head dealing", "no"]

def trap():
    damage = rand.randint(1,5)
    random_trap = rand.choice(traps)
    print(f"{random_trap} {damage} damage")

trap()
