import turtle as trtl
import random
from render import *
import time
import math
#Stats declaration (in the future read a stats.txt)
player_hp = 1000
player_maxhp = player_hp
player_speed = 1000
player_power = 1000
player_ult = 0
player_name = ''
enemy_hp = 1000
enemy_maxhp = enemy_hp
enemy_speed = 1000
enemy_power = 1000
enemy_name = ''
flex_count = 0
player_attacks = ["","Free Throw", "Drink Up", "Shmoney Dance", "Final Dunk"]
enemy_attacks = ["Nae Nae", "Flex", "Whip", "Heal"]
potion_count = 4
player_choice = 0
player_constant = 0

# LOL FART

# LOL POOP
#functions
#types the ACTION
def fireball_animation():
    tempshape = player_shape
    wn.tracer(False)
    fireball.setheading(0)
    fireball.goto(-500,375)
    fireball.shape('gamefireball.gif')
    fireball.showturtle()
    wn.tracer(True)
    player.shape('wizardogymouth.gif')
    fireball.goto(200,245)
    fireball.shape('explosion1.gif')
    time.sleep(.05)
    fireball.shape('explosion2.gif')
    time.sleep(.05)
    fireball.shape('explosion3.gif')
    time.sleep(.05)
    player.shape(tempshape)
    fireball.hideturtle()

def fireball_animation_fail():
    tempshape = player_shape
    wn.tracer(False)
    fireball.setheading(0)
    fireball.goto(-500,375)
    fireball.shape('gamefireball.gif')
    fireball.showturtle()
    wn.tracer(True)
    player.shape('wizardogymouth.gif')
    temp = random.randint(200,500)
    fireball.goto(-200,temp)
    fireball.shape('explosion1.gif')
    time.sleep(.05)
    fireball.shape('explosion2.gif')
    time.sleep(.05)
    fireball.shape('explosion3.gif')
    time.sleep(.05)
    player.shape(tempshape)
    fireball.hideturtle()

def setenemyfile(x):
    global enemy_name, enemy_hp, enemy_speed, enemy_power, enemy_maxhp, enemy_shape
    with open(x, 'r') as file:
        stats = file.readlines()
    enemy_name = str(stats[0]).rstrip('\n')
    enemy_hp = int(stats[1])
    enemy_speed = int(stats[2])
    enemy_power = int(stats[3])
    wn.addshape(str(stats[4]).rstrip('\n'))
    enemy_shape = (str(stats[4]).rstrip('\n'))
    enemy.shape(enemy_shape)
    enemy_maxhp = enemy_hp

def setplayerfile(x):
    global player_name, player_hp, player_speed, player_power, player_maxhp, player_shape
    with open(x, 'r') as file:
        stats = file.readlines()
    player_name = str(stats[0]).rstrip('\n')
    player_hp = int(stats[1])
    player_speed = int(stats[2])
    player_power = int(stats[3])
    wn.addshape(str(stats[4]).rstrip('\n'))
    player_shape = (str(stats[4]).rstrip('\n'))
    player.shape(player_shape)
    player_maxhp = player_hp

def playerchoose():
    global player_constant, menu_status
    if (menu_status == "home") and ((enemy_hp > 0) and (player_hp > 0)):
        if(player_constant == 0):
            hp_update()
            type_fight("Select "+ player_name+"'s Attack: ")
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
    wn.onkey(uselesslol,"1")
    wn.onkey(uselesslol,"2")
    wn.onkey(uselesslol,"3")
    wn.onkey(uselesslol,"4")
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((enemy_hp > 0) and (player_hp > 0))):
        player_choice = 1
        speedcheck()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def choice_two():
    wn.onkey(uselesslol,"1")
    wn.onkey(uselesslol,"2")
    wn.onkey(uselesslol,"3")
    wn.onkey(uselesslol,"4")
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((enemy_hp > 0) and (player_hp > 0))):
        player_choice = 2
        playerattack()
        enemyattack()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def choice_three():
    wn.onkey(uselesslol,"1")
    wn.onkey(uselesslol,"2")
    wn.onkey(uselesslol,"3")
    wn.onkey(uselesslol,"4")
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((enemy_hp > 0) and (player_hp > 0))):
        player_choice = 3
        speedcheck()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def choice_four():
    wn.onkey(uselesslol,"1")
    wn.onkey(uselesslol,"2")
    wn.onkey(uselesslol,"3")
    wn.onkey(uselesslol,"4")
    global player_constant
    global player_choice
    global menu_status
    wn.onkey(flag_state_shop,"b")
    if ((menu_status == "home") and ((enemy_hp > 0) and (player_hp > 0))):
        player_choice = 4
        speedcheck()
        hpcheck()
        player_constant = 0
    else:
        useless.forward(1)
def playerattack():
    global player_choice, player_attacks, player_hp, player_speed, player_power, player_ult, enemy_hp, enemy_attacks, enemy_speed, enemy_power, menu_status, potion_count
    tempplayer = player_attacks[player_choice]
    if menu_status == "home":
        if player_hp > 0:
            if tempplayer == "Free Throw":
                type_fight(player_name+" shot a fireball!")
                tempn = random.randint(1,1000)
                tempd = str(player_power)
                if tempn in range(1,801):
                    temppower = player_power
                    fireball_animation()
                    type_fight(player_name+" hit the enemy!")
                    tempmsg = str(enemy_name+" took " + tempd + " damage!")
                    if player_ult < 100:
                        player_ult += 10
                    player_power = temppower
                    type_fight(tempmsg)
                    enemy_hp = enemy_hp - player_power
                elif tempn in range (800,1001):
                    fireball_animation_fail()
                    type_fight(player_name+" missed the enemy!")
                hp_update()
            elif tempplayer == "Drink Up":
                if potion_count > 0:
                    type_fight(player_name+" drank a potion!")
                    if (player_hp == 200):
                        type_fight("But it failed!")
                    elif (player_hp < 200):
                        type_fight(player_name+" restored to full hp!")
                        player_hp = 200
                    potion_count -= 1
                if potion_count == 0:
                    type_fight("No potions left!")
                hp_update()
            elif tempplayer == "Shmoney Dance":
                type_fight(player_name+"'s speed doubled from power up!")
                player_speed = 2 * player_speed
            elif tempplayer == "Final Dunk":
                if player_ult > 99:
                    type_fight(player_name+" tried to do a final strike...")
                    type_fight(player_name+" charged up energy!")
                    type_fight(player_name+" demolished the enemy!")
                    enemy_hp = 0
                    hp_update()
                else:
                    type_fight(player_name+" tried to do a final strike...")
                    type_fight("But it failed! (Ult meter too low)")
    else:
        useless.forward(1)

def hpcheck():
    global player_hp, enemy_hp
    if player_hp <= 0:
        type_fight(player_name+" fainted! Game Over!")
        enemy_hp = 0
    elif enemy_hp <= 0:
        type_fight(enemy_name +" fainted! You Won!")

def healthbar_update():
    global player_hp, player_maxhp
    if (player_hp/player_maxhp) > (3/4):
        healthbar.showturtle()
        healthbar.shape('healthbar1.gif')
    elif ((player_hp/player_maxhp) > 1/2) and ((player_hp/player_maxhp) <= (3/4)):
        healthbar.showturtle()
        healthbar.shape('healthbar2.gif')
    elif ((player_hp/player_maxhp) > 1/4) and ((player_hp/player_maxhp) <= (1/2)):
        healthbar.showturtle()
        healthbar.shape('healthbar3.gif')
    elif(player_hp/player_maxhp) > 0 and ((player_hp/player_maxhp) <= (1/4)):
        healthbar.showturtle()
        healthbar.shape('healthbar4.gif')
    else:
        healthbar.hideturtle()
        
def ultbar_update():
    global player_ult
    if (player_ult) == 100:
        ultbar.showturtle()
        ultbar.shape('ultimatebar1.gif')
    elif ((player_ult) > 60) and (player_ult) <= 90:
        ultbar.showturtle()
        ultbar.shape('ultimatebar2.gif')
    elif ((player_ult) > 30) and ((player_ult) <= 60):
        ultbar.showturtle()
        ultbar.shape('ultimatebar3.gif')
    elif((player_ult) > 0) and ((player_ult) <= 30):
        ultbar.showturtle()
        ultbar.shape('ultimatebar4.gif')
    else:
        ultbar.hideturtle()

def hp_update():
    global player_hp, enemy_hp, player_ult, player_maxhp
    wn.tracer(False)
    player_hptxt.clear()
    enemy_hptxt.clear()
    ultimate_text.clear()
    player_hptxt.write("HP: " + str(player_hp) + "/" + str(player_maxhp), font=("Impact", 20, "bold"))
    enemy_hptxt.write("ENEMY HP: " + str(enemy_hp) + "/" + str(enemy_maxhp), font=("Impact", 20, "bold"))
    ultimate_text.write("FINAL STRIKE: " + str(player_ult) + "/100", font=("Impact", 20, "bold"))
    healthbar_update()
    ultbar_update()
    wn.tracer(True)

def enemyattack():
    global player_attacks, player_hp, player_speed, player_power, player_ult, enemy_hp, enemy_attacks, enemy_speed, enemy_power, flex_count
    if enemy_hp > 160:
        i_enemy = random.randint(0,2)
    else:
        i_enemy = random.randint(0,3)
    crit = random.randint(0,100)
    if crit == 13:
        type_fight("A critical hit!")
        enemy_power *= 2
    j = enemy_attacks[i_enemy]
    if j == "Heal":
        type_fight(enemy_name +" restored 50 hp")
        enemy_hp = enemy_hp + 50
        hp_update()
    elif j == "Nae Nae":
        type_fight(enemy_name + " growled at "+player_name+"!")
        type_fight(player_name+"'s speed dropped by 20!")
        player_speed = player_speed - 20
    elif j == "Whip":
        type_fight(player_name+" got clubbed!")
        tempd = str(enemy_power)
        slash_animation()
        tempmsg = str(player_name+" lost "+tempd+" HP!")
        type_fight(tempmsg)
        player_hp = player_hp - enemy_power
        if player_ult < 100:
            player_ult += 10
        hp_update()
    elif j == "Flex":
        flex_count += 1
        if flex_count > 3:
            type_fight(player_name+" got clubbed!")
            tempd = str(enemy_power)
            slash_animation()
            tempmsg = str(player_name+" lost "+tempd+" HP!")
            type_fight(tempmsg)
            player_hp = player_hp - enemy_power
            if player_ult < 100:
                player_ult += 10
            hp_update()
        else:
            type_fight(enemy_name + " flexed!")
            type_fight(enemy_name+"'s attacks do 1.1x damage!")
            enemy_power = math.floor(1.1 * enemy_power)
    if crit == 13:
        enemy_power /= 2

def speedcheck():
    global player_speed
    global enemy_speed
    global menu_status
    if menu_status == "home":
        if (player_speed - enemy_speed) == 0:
            tempr = random.randint(0,1)
            if tempr == 1:
                playerattack()
                enemyattack()
            elif tempr == 0:
                enemyattack()
                playerattack()
        elif (player_speed - enemy_speed) > 0:
            playerattack()
            enemyattack()
        elif (player_speed - enemy_speed) < 0:
            enemyattack()
            playerattack()
    else:
        useless.forward(1)

def flag_state_shop():
    global menu_status
    menu_status = 'shop'
def flag_state_home():
    global menu_status
    menu_status = 'home'