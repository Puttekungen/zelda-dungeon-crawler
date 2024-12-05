import random as rand
from func.classes import Player

def trap(player): # Gör så att användaren tar skada när den går in i en av fällorna
    traps = ["You got shot by a hidden crossbow and took ", "You step on a hidden pressure plate and a metal chest falls from the ceiling hiting you in the head dealing", 
         "You stepped on a hidden trapdoor and landed on spikes, you took", "You walked in on a witch and she threw poison on you dealing"]
    damage = rand.randint(1,5)
    random_trap = rand.choice(traps)
    player.hp -= damage
    print(f"{random_trap} {damage} damage")
    resume = input("press 'enter' to continue\n\n")