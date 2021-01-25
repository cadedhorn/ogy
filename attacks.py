import turtle as trtl
import random
# funny

shaq_hp = 200
beet_attacks = ["nae nae", "whip", "flex", "heal"]
i_beet = random.randint(0,3)
j = beet_attacks[i_beet]
if j in beet_attacks:
    shaq_hp -= 50
    print("Shaq took 50 damage!")


print(beet_attacks[i_beet])