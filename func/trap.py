import random as rand

traps = ["You got shot by a hidden crossbow and took ", "You step on a hidden pressure plate and a metal chest falls from the ceiling hiting you in the head dealing", "You stepes on a hidden trap dorr and landed on spikes, you took", "You walked in on a witch and she threw poison on you dealing"]

def trap():
    damage = rand.randint(1,5)
    random_trap = rand.choice(traps)
    print(f"{random_trap} {damage} damage")

trap()
