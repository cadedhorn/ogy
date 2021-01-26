import turtle as trtl
import random
# funny ogy

#Stats declaration (in the future read a stats.txt)
shaq_hp = 200
shaq_speed = 100
beet_hp = 200
beet_speed = 200
shaq_attacks = ["","free throw", "drink up", "shmoney dance", "final dunk"]
beet_attacks = ["nae nae", "whip", "flex", "heal"]

#functions
def shaqattack():
    global shaq_attacks, shaq_hp, shaq_speed, beet_hp, beet_attacks, beet_speed
    print("")
    i = int(input("WTF ATTACK YOU WANNA DO HOMIE: "))
    if i not in range (1,4):
        print("Invalid number, defaulting to first attack")
        i = 1
    tempshaq = shaq_attacks[i]
    if tempshaq == "free throw":
        print("You shot a free throw!")
        print("Beet took 50 damage!")
        beet_hp -= 50
    elif tempshaq == "drink up":
        print("You drank dat gatorade!")
        if shaq_hp == 200:
            print("But it failed!")
        elif shaq_hp + 50 > 200:
            print("You restored", 200 - shaq_hp, "hp!")
            shaq_hp = 200
        elif shaq_hp + 50 <= 200:
            print("You restored 50 hp!")
            shaq_hp += 50
    elif tempshaq == "shmoney dance":
        print("Shaq's speed doubled from the shmoney dance!")
        shaq_speed = 2 * shaq_speed
    elif tempshaq == "final dunk":
        print("Shaq leaps into the air!")
        print("Shaq slam dunked on beet!")
        beet_hp = 0

def hpcheck():
    global shaq_hp, beet_hp
    if shaq_hp <= 0:
        print("Shaq fainted!")
        beet_hp = 0
    elif beet_hp <= 0:
        print("Beet fainted!")

def beetattack():
    global shaq_attacks, shaq_hp, shaq_speed, beet_hp, beet_attacks, beet_speed
    if beet_hp > 160:
        i_beet = random.randint(0,2)
    else:
        i_beet = random.randint(0,3)
    j = beet_attacks[i_beet]
    if j == "heal":
        print("Beet restored a cuppa hp")
        beet_hp += 50
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

def speedcheck():
    global shaq_speed
    global beet_speed
    if shaq_speed - beet_speed == 0:
        tempr = random.randint(0,1)
        if tempr == 1:
            shaqattack()
            beetattack()
        if tempr == 0:
            beetattack()
            shaqattack()
    if shaq_speed - beet_speed > 0:
        shaqattack()
        beetattack()
    if shaq_speed - beet_speed < 0:
        beetattack()
        shaqattack()

while beet_hp > 0:
    speedcheck()
    hpcheck()