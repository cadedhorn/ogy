import turtle as trtl
import random
from render import *
import time
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
shaq_constant = 0
# LOL FART

# LOL POOP
#functions
#types the ACTION
def shaqchoose():
    global shaq_constant
    if (menu_status == "home") and ((beet_hp > 0) and (shaq_hp > 0)):
        if(shaq_constant == 0):
            type_fight("WTF ATTACK YOU WANNA DO HOMIE: ")
            wn.onkey(choice_one,"1")
            wn.onkey(choice_two,"2")
            wn.onkey(choice_three,"3")
            wn.onkey(choice_four,"4")
            wn.listen()
            shaq_constant = 1   
        else:
            useless.forward(1)
    else:
        useless.forward(1)
def choice_one():
    global shaq_constant
    global shaq_choice
    if (menu_status == "home") and ((beet_hp > 0) and (shaq_hp > 0)):
        shaq_choice = 1
        speedcheck()
        hpcheck()
        shaq_constant = 0
def choice_two():
    global shaq_constant
    global shaq_choice
    if (menu_status == "home") and ((beet_hp > 0) and (shaq_hp > 0)):
        shaq_choice = 2
        speedcheck()
        hpcheck()
        shaq_constant = 0
def choice_three():
    global shaq_constant
    global shaq_choice
    if (menu_status == "home") and ((beet_hp > 0) and (shaq_hp > 0)):
        shaq_choice = 3
        speedcheck()
        hpcheck()
        shaq_constant = 0
def choice_four():
    global shaq_constant
    global shaq_choice
    if (menu_status == "home") and ((beet_hp > 0) and (shaq_hp > 0)):
        shaq_choice = 4
        speedcheck()
        hpcheck()
        shaq_constant = 0

def shaqattack():
    global shaq_choice, shaq_attacks, shaq_hp, shaq_speed, shaq_power, beet_hp, beet_attacks, beet_speed, beet_power
    tempshaq = shaq_attacks[shaq_choice]
    if tempshaq == "Free Throw":
        type_fight("You shot a free throw!")
        tempd = str(shaq_power)
        tempmsg = str("Beet took " + tempd + " damage!")
        type_fight(tempmsg)
        beet_hp = beet_hp - shaq_power
    elif tempshaq == "Drink Up":
        type_fight("You drank dat gatorade!")
        if (shaq_hp == 200):
            type_fight("But it failed!")
        elif (shaq_hp + 50) > 200:
            tempj = str(200 - shaq_hp)
            tempmsg = str("You restored "+tempj+" hp!")
            type_fight(tempmsg)
            shaq_hp = 200
        elif (shaq_hp + 50) <= 200:
            type_fight("You restored 50 hp!")
            shaq_hp = shaq_hp + 50
    elif tempshaq == "Shmoney Dance":
        type_fight("Shaq's speed doubled from the shmoney dance!")
        shaq_speed = 2 * shaq_speed
    elif tempshaq == "Final Dunk":
        type_fight("Shaq leaps into the air!")
        type_fight("Shaq slam dunked on Beet!")
        beet_hp = 0

def hpcheck():
    global shaq_hp, beet_hp
    if shaq_hp <= 0:
        type_fight("Shaq fainted!")
        beet_hp = 0
    elif beet_hp <= 0:
        type_fight("Beet fainted!")

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
        type_fight("Beet restored a cuppa hp")
        beet_hp = beet_hp + 50
    elif j == "Nae Nae":
        type_fight("Beet nae nae'd on you!")
        type_fight("Your speed dropped by 20!")
        shaq_speed = shaq_speed - 20
    elif j == "Whip":
        type_fight("Shaq got whipped!")
        tempd = str(beet_power)
        tempmsg = str("Shaq lost "+tempd+" hp!")
        type_fight(tempmsg)
        shaq_hp = shaq_hp - beet_power
    elif j == "Flex":
        type_fight("Beet flexed!")
        type_fight("Beet's attacks do twice as much damage!")
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