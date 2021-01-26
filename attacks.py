import turtle as trtl
import random
# funny ogy

#Stats declaration (in the future read a stats.txt)
shaq_hp = 200
shaq_speed = 100
beet_hp = 200
beet_speed = 200
beet_attacks = ["nae nae", "whip", "flex", "heal"]

if beet_hp > 160:
    i_beet = random.randint(0,2)
else:
    i_beet = random.randint(0,3)
j = beet_attacks[i_beet]
if j == "heal":
    print("Beet restored a cuppa hp")
elif j == "nae nae":
    print("Beet nae nae'd on you!")
    print("Your speed dropped by 20!")
    shaq_speed -= 20
elif j == "whip":
    print("Shaq got whipped!")
    print("Shaq lost 50 hp!")
    shaq_hp -= 50
elif j == "flex":
    print("Beet flexed!")
    print("Beet's attacks do twice as much damage!")