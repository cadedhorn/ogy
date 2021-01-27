import turtle as trtl
import random
import main
#Stats declaration (in the future read a stats.txt)
shaq_hp = 200
shaq_speed = 100
shaq_power = 50
beet_hp = 200
beet_speed = 200
beet_power = 50
shaq_attacks = ["","Free Throw", "Drink Up", "Shmoney Dance", "Final Dunk"]
beet_attacks = ["Nae Nae", "Whip", "Flex", "Heal"]
shaq_choice = 0
#random.seed(9812345761982873654786124534647152)

#functions
def shaqchoose():
    global shaq_choice, shaq_attacks, shaq_hp, shaq_speed, shaq_power, beet_hp, beet_attacks, beet_speed, beet_power
    main.type_fight("WTF ATTACK YOU WANNA DO HOMIE: ")
        
def choice_one():
    if (main.menu_status == "home"):
        shaq_choice = "Free Throw"
        speedcheck()
        hpcheck()
def choice_two():
    if (main.menu_status == "home"):
        shaq_choice = "Drink Up"
        speedcheck()
        hpcheck()
def choice_three():
    if (main.menu_status == "home"):
        shaq_choice = "Shmoney Dance"
        speedcheck()
        hpcheck()
def choice_four():
    if (main.menu_status == "home"):
        shaq_choice = "Final Dunk"
        speedcheck()
        hpcheck()

def shaqattack():
    global shaq_choice, shaq_attacks, shaq_hp, shaq_speed, shaq_power, beet_hp, beet_attacks, beet_speed, beet_power
    tempshaq = shaq_attacks[shaq_choice]
    crit = random.randint(0,100)
    if tempshaq == "Free Throw":
        main.type_fight("You shot a free throw!")
        main.type_fight("Beet took", shaq_power, "damage!")
        beet_hp = beet_hp - shaq_power
    elif tempshaq == "Drink Up":
        main.type_fight("You drank dat gatorade!")
        if (shaq_hp == 200):
            main.type_fight("But it failed!")
        elif (shaq_hp + 50) > 200:
            main.type_fight("You restored", 200 - shaq_hp, "hp!")
            shaq_hp = 200
        elif (shaq_hp + 50) <= 200:
            main.type_fight("You restored 50 hp!")
            shaq_hp = shaq_hp + 50
    elif tempshaq == "Shmoney Dance":
        main.type_fight("Shaq's speed doubled from the shmoney dance!")
        shaq_speed = 2 * shaq_speed
    elif tempshaq == "Final Dunk":
        main.type_fight("Shaq leaps into the air!")
        main.type_fight("Shaq slam dunked on beet!")
        beet_hp = 0
    if crit == 87:
        shaq_power /= 2

def hpcheck():
    global shaq_hp, beet_hp
    if shaq_hp <= 0:
        main.type_fight("Shaq fainted!")
        beet_hp = 0
    elif beet_hp <= 0:
        main.type_fight("Beet fainted!")

def beetattack():
    global shaq_attacks, shaq_hp, shaq_speed, shaq_power, beet_hp, beet_attacks, beet_speed, beet_power
    if beet_hp > 160:
        i_beet = random.randint(0,2)
    else:
        i_beet = random.randint(0,3)
    crit = random.randint(0,100)
    if crit == 13:
        print("A critical hit!")
        beet_power *= 2
    j = beet_attacks[i_beet]
    if j == "Heal":
        main.type_fight("Beet restored a cuppa hp")
        beet_hp = beet_hp + 50
    elif j == "Nae Nae":
        main.type_fight("Beet nae nae'd on you!")
        main.type_fight("Your speed dropped by 20!")
        shaq_speed = shaq_speed - 20
    elif j == "Whip":
        main.type_fight("Shaq got whipped!")
        main.type_fight("Shaq lost", beet_power, "hp!")
        shaq_hp = shaq_hp - beet_power
    elif j == "Flex":
        main.type_fight("Beet flexed!")
        main.type_fight("Beet's attacks do twice as much damage!")
        beet_power = 2 * beet_power
    if crit == 13:
        beet_power /= 2

def speedcheck():
    global shaq_speed
    global beet_speed
    if (shaq_speed - beet_speed) == 0:
        tempr = random.randint(0,1)
        if tempr == 1:
            shaqattack()
            beetattack()
        elif tempr == 0:
            beetattack()
            shaqattack()
    elif (shaq_speed - beet_speed) > 0:
        shaqattack()
        beetattack()
    elif (shaq_speed - beet_speed) < 0:
        beetattack()
        shaqattack()
