import turtle as trtl
import random
# funny ogy 3

#Stats declaration (in the future read a stats.txt)
shaq_hp = 200
shaq_speed = 100
shaq_power = 50
beet_hp = 200
beet_speed = 200
beet_power = 50
shaq_attacks = ["","Free Throw", "Drink Up", "Shmoney Dance", "Final Dunk"]
beet_attacks = ["Nae Nae", "Whip", "Flex", "Heal"]
random.seed(9812345761982873654786124534647152)

#functions
def shaqattack():
    global shaq_attacks, shaq_hp, shaq_speed, shaq_power, beet_hp, beet_attacks, beet_speed, beet_power
    print("")
    i = int(input("WTF ATTACK YOU WANNA DO HOMIE: "))
    if i not in range (1,5):
        print("Invalid number, defaulting to first attack")
        i = 1
    tempshaq = shaq_attacks[i]
    if tempshaq == "Free Throw":
        print("You shot a free throw!")
        print("Beet took", shaq_power, "damage!")
        beet_hp -= shaq_power
    elif tempshaq == "Drink Up":
        print("You drank dat gatorade!")
        if shaq_hp == 200:
            print("But it failed!")
        elif shaq_hp + 50 > 200:
            print("You restored", 200 - shaq_hp, "hp!")
            shaq_hp = 200
        elif shaq_hp + 50 <= 200:
            print("You restored 50 hp!")
            shaq_hp += 50
    elif tempshaq == "Shmoney Dance":
        print("Shaq's speed doubled from the shmoney dance!")
        shaq_speed = 2 * shaq_speed
    elif tempshaq == "Final Dunk":
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
    global shaq_attacks, shaq_hp, shaq_speed, shaq_power, beet_hp, beet_attacks, beet_speed, beet_power
    if beet_hp > 160:
        i_beet = random.randint(0,2)
    else:
        i_beet = random.randint(0,3)
    j = beet_attacks[i_beet]
    if j == "Heal":
        print("Beet restored a cuppa hp")
        beet_hp += 50
    elif j == "Nae Nae":
        print("Beet nae nae'd on you!")
        print("Your speed dropped by 20!")
        shaq_speed -= 20
    elif j == "Whip":
        print("Shaq got whipped!")
        print("Shaq lost", beet_power, "hp!")
        shaq_hp -= beet_power
    elif j == "Flex":
        print("Beet flexed!")
        print("Beet's attacks do twice as much damage!")
        beet_power = 2 * beet_power

def speedcheck():
    global shaq_speed
    global beet_speed
    if shaq_speed - beet_speed == 0:
        tempr = random.randint(0,1)
        if tempr == 1:
            shaqattack()
            beetattack()
        elif tempr == 0:
            beetattack()
            shaqattack()
    elif shaq_speed - beet_speed > 0:
        shaqattack()
        beetattack()
    elif shaq_speed - beet_speed < 0:
        beetattack()
        shaqattack()

while beet_hp > 0:
    speedcheck()
    hpcheck()