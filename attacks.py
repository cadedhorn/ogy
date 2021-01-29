import turtle as trtl
import random
from render import *
import time
import math
#Stats declaration (in the future read a stats.txt)
player_hp = 200
player_maxhp = player_hp
player_speed = 100
player_power = 50
player_ult = 0
beet_hp = 400
beet_maxhp = beet_hp
beet_speed = 200
beet_power = 50
player_attacks = ["","Free Throw", "Drink Up", "Shmoney Dance", "Final Dunk"]
beet_attacks = ["Nae Nae", "Flex", "Whip", "Heal"]
player_choice = 0
player_constant = 0

# LOL FART

# LOL POOP
#functions
#types the ACTION
def playerchoose():
    global player_constant, menu_status
    if (menu_status == "home") and ((beet_hp > 0) and (player_hp > 0)):
        if(player_constant == 0):
            hp_update()
            type_fight("Select player's Attack: ")
            wn.onkey(choice_one,"1")
            wn.onkey(choice_two,"2")
            wn.onkey(choice_three,"3")
            wn.onkey(choice_four,"4")
            wn.onkey(flag_state_shop,"b")
            wn.listen()
            player_constant = 1   
        else:
            useless.forward(1)
    else:
        wn.onkey(flag_state_home, "a")
        useless.forward(1)
def choice_one():
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((beet_hp > 0) and (player_hp > 0))):
        player_choice = 1
        speedcheck()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def choice_two():
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((beet_hp > 0) and (player_hp > 0))):
        player_choice = 2
        playerattack()
        beetattack()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def choice_three():
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((beet_hp > 0) and (player_hp > 0))):
        player_choice = 3
        speedcheck()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def choice_four():
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((beet_hp > 0) and (player_hp > 0))):
        player_choice = 4
        speedcheck()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def playerattack():
    global player_choice, player_attacks, player_hp, player_speed, player_power, player_ult, beet_hp, beet_attacks, beet_speed, beet_power, menu_status
    tempplayer = player_attacks[player_choice]
    if menu_status == "home":
        if player_hp > 0:
            if tempplayer == "Free Throw":
                type_fight("You shot a fireball!")
                tempn = random.randint(1,1000)
                tempd = str(player_power)
                if tempn in range(1,528):
                    temppower = player_power
                    type_fight("you hit the enemy!")
                    tempmsg = str("Beet took " + tempd + " damage!")
                    player_ult += 10
                    player_power = temppower
                    type_fight(tempmsg)
                    beet_hp = beet_hp - player_power
                elif tempn in range (527,1001):
                    temppower = player_power
                    type_fight("you missed the enemy!")
                    tempmsg = str("Beet took 0 damage!")
                    player_power = 0
                    type_fight(tempmsg)
                    beet_hp = beet_hp - player_power
                    player_power = temppower
                hp_update()
            elif tempplayer == "Drink Up":
                type_fight("you drank a gatorade!")
                if (player_hp == 200):
                    type_fight("But it failed!")
                elif (player_hp < 200):
                    type_fight("you restored to full hp!")
                    player_hp = 200
                hp_update()
            elif tempplayer == "Shmoney Dance":
                type_fight("your speed doubled from power up!")
                player_speed = 2 * player_speed
            elif tempplayer == "Final Dunk":
                if player_ult > 99:
                    type_fight("you tried to do a final strike...")
                    type_fight("you charged up energy!")
                    type_fight("you demolished the enemy!")
                    beet_hp = 0
                    hp_update()
                else:
                    type_fight("you tried to do a final strike...")
                    type_fight("But it failed! (Ult meter too low)")
    else:
        useless.forward(1)

def hpcheck():
    global player_hp, beet_hp
    if player_hp <= 0:
        type_fight("you fainted! Game Over!")
        beet_hp = 0
    elif beet_hp <= 0:
        type_fight("Beet fainted! You Won!")

def hp_update():
    global player_hp, beet_hp, player_ult
    wn.tracer(False)
    player_hptxt.clear()
    enemy_hptxt.clear()
    ultimate_text.clear()
    player_hptxt.write("HP: " + str(player_hp) + "/" + str(player_maxhp), font=("Impact", 20, "bold"))
    enemy_hptxt.write("ENEMY HP: " + str(beet_hp) + "/" + str(beet_maxhp), font=("Impact", 20, "bold"))
    ultimate_text.write("FINAL STRIKE: " + str(player_ult) + "/100", font=("Impact", 20, "bold"))
    wn.tracer(True)

def beetattack():
    global player_attacks, player_hp, player_speed, player_power, player_ult, beet_hp, beet_attacks, beet_speed, beet_power
    flex_count = 0
    if beet_hp > 160:
        i_beet = random.randint(0,2)
    else:
        i_beet = random.randint(0,3)
    crit = random.randint(0,100)
    if crit == 13:
        type_fight("A critical hit!")
        beet_power *= 2
    j = beet_attacks[i_beet]
    if j == "Heal":
        type_fight("Beet restored a cuppa hp")
        beet_hp = beet_hp + 50
        hp_update()
    elif j == "Nae Nae":
        type_fight("Beet nae nae'd on you!")
        type_fight("Your speed dropped by 20!")
        player_speed = player_speed - 20
    elif j == "Whip":
        type_fight("you got whipped!")
        tempd = str(beet_power)
        tempmsg = str("you lost "+tempd+" HP!")
        type_fight(tempmsg)
        player_hp = player_hp - beet_power
        player_ult += 10
        hp_update()
    elif j == "Flex":
        flex_count += 1
        if flex_count > 3:
            type_fight("you got whipped!")
            tempd = str(beet_power)
            tempmsg = str("you lost "+tempd+" HP!")
            type_fight(tempmsg)
            player_hp = player_hp - beet_power
            player_ult += 10
            hp_update()
        else:
            type_fight("Beet flexed!")
            type_fight("Beet's attacks do 1.1x damage!")
            beet_power = math.floor(1.1 * beet_power)
    if crit == 13:
        beet_power /= 2

def speedcheck():
    global player_speed
    global beet_speed
    global menu_status
    if menu_status == "home":
        if (player_speed - beet_speed) == 0:
            tempr = random.randint(0,1)
            if tempr == 1:
                playerattack()
                beetattack()
            elif tempr == 0:
                beetattack()
                playerattack()
        elif (player_speed - beet_speed) > 0:
            playerattack()
            beetattack()
        elif (player_speed - beet_speed) < 0:
            beetattack()
            playerattack()
    else:
        useless.forward(1)

def flag_state_shop():
    global menu_status
    menu_status = 'shop'
def flag_state_home():
    global menu_status
    menu_status = 'home'