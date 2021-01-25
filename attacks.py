import turtle as trtl
import random


shaq_hp = 200
beet_attacks = ["nae nae", "whip", "flex", "heal"]
i_beet = random.randint(0,3)
j = beet_attacks[i_beet]
if j == "nae nae":
    shaq_hp -= 50
    print("Shaq took 50 damage!")


print(attacks[i])