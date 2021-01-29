import turtle as trtl
import random
import time
#--------Setup--------

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape('fancyshaq.gif')
wn.addshape('slash1.gif')
wn.addshape('slash2.gif')
wn.addshape('slash3.gif')
wn.addshape('slash4.gif')
wn.addshape('slash5.gif')
wn.addshape('slash6.gif')
wn.addshape('slash7.gif')
wn.addshape('healthbar1.gif')
wn.addshape('healthbar2.gif')
wn.addshape('healthbar3.gif')
wn.addshape('healthbar4.gif')
wn.addshape('ultimatebar1.gif')
wn.addshape('ultimatebar2.gif')
wn.addshape('ultimatebar3.gif')
wn.addshape('ultimatebar4.gif')
wn.addshape('explosion1.gif')
wn.addshape('explosion2.gif')
wn.addshape('explosion3.gif')
wn.addshape('gamefireball.gif')
wn.addshape('wizardogymouth.gif')
wn.addshape('enemyhealthbar1.gif')
wn.addshape('enemyhealthbar2.gif')
wn.addshape('enemyhealthbar3.gif')
wn.addshape('enemyhealthbar4.gif')
wn.addshape('enemyhealthbar5.gif')
wn.addshape('enemyhealthbar6.gif')
wn.addshape('enemyhealthbar7.gif')
wn.addshape('enemyhealthbar8.gif')
wn.addshape('enemyhealthbar9.gif')
wn.addshape('enemyhealthbar10.gif')
wn.addshape('potionbar1.gif')
wn.addshape('potionbar2.gif')
wn.addshape('potionbar3.gif')
wn.bgpic("paperbackground.gif")

wn.tracer(False)

#makes all turtles used in the program
enemy = trtl.Turtle()
enemy.hideturtle()
enemy.pu() #LOL FART
enemy.goto(200,245)

player = trtl.Turtle()
player.hideturtle()
player.pu()
player.goto(-500,375)

drawer = trtl.Turtle()
drawer.pensize(5)
drawer.speed(0)
drawer.hideturtle()

fancyshaq = trtl.Turtle()
fancyshaq.hideturtle()
fancyshaq.pu()
fancyshaq.shape('fancyshaq.gif')
fancyshaq.goto(0,195)


box_1 = trtl.Turtle()
box_2 = trtl.Turtle()
box_3 = trtl.Turtle()
box_4 = trtl.Turtle()

box_1.pu()
box_2.pu()
box_3.pu()
box_4.pu()

box_1.speed(0)
box_2.speed(0)
box_3.speed(0)
box_4.speed(0)

box_1.hideturtle()
box_2.hideturtle()
box_3.hideturtle()
box_4.hideturtle()

player_hptxt = trtl.Turtle()
gatorade_text = trtl.Turtle()
ultimate_text = trtl.Turtle()
enemy_hptxt = trtl.Turtle()

player_hptxt.hideturtle()
gatorade_text.hideturtle()
ultimate_text.hideturtle()
enemy_hptxt.hideturtle()

player_hptxt.pu()
gatorade_text.pu()
ultimate_text.pu()
enemy_hptxt.pu()

player_hptxt.speed(0)
gatorade_text.speed(0)
ultimate_text.speed(0)
enemy_hptxt.speed(0)

player_hptxt.goto(-700,200)
gatorade_text.goto(-700,100)
ultimate_text.goto(-700,0)
enemy_hptxt.goto(-250,0)

bobux_counter = trtl.Turtle()
bobux_counter.pu()
bobux_counter.hideturtle()
bobux_counter.goto(-700,-475)

slash = trtl.Turtle()
slash.pu()
slash.hideturtle()
slash.goto(-500,375)

fireball = trtl.Turtle()
fireball.pu()
fireball.hideturtle()
fireball.goto(-500,375)
fireball.speed(5)

healthbar = trtl.Turtle()
healthbar.shape('healthbar1.gif')
healthbar.pu()
healthbar.hideturtle()
healthbar.goto(-500,175)

ultbar = trtl.Turtle()
ultbar.shape('ultimatebar1.gif')
ultbar.hideturtle()
ultbar.pu()
ultbar.goto(-500,-25)

potionbar = trtl.Turtle()
potionbar.shape('potionbar1.gif')
potionbar.hideturtle()
potionbar.pu()
potionbar.goto(-500,75)

enemyhealthbar = trtl.Turtle()
enemyhealthbar.shape('enemyhealthbar1.gif')
enemyhealthbar.pu()
enemyhealthbar.hideturtle()
enemyhealthbar.goto(200,-25)

commentator = trtl.Turtle()
commentator.hideturtle()
commentator.pu()
commentator.goto(-690,-147)

useless = trtl.Turtle() # SUPER BAD NAME THIS IS LITERALLY THE MOST INTEGRAL PART OF THE WHOLE PROGRAM IT DOESNT WORK WITHOUT IT
useless.up()
useless.hideturtle()

loader = trtl.Turtle()
loader.up()
loader.pensize(60)
loader.speed(0)

wn.tracer(True)

#sets up global variables that are used throughout the game
global bobux
bobux = 0

#very important status value to check when certain functions can or can not happen
global menu_status
menu_status = 'placeholder'

#used to customize bottom text 
global button_list
button_list = []

global fight_text
fight_text = "if you're seeing this, the game broke"

global current_text
current_text = "If you're seeing this, the game broke"
#--------Functions--------    
def uselesslol():
    useless.forward(1)

def slash_animation():
    slash.shape('slash1.gif')
    slash.showturtle()
    time.sleep(.05)
    slash.shape('slash2.gif')
    time.sleep(.05)
    slash.shape('slash3.gif')
    time.sleep(.05)
    slash.shape('slash4.gif')
    time.sleep(.05)
    slash.shape('slash5.gif')
    time.sleep(.05)
    slash.shape('slash6.gif')
    time.sleep(.05)
    slash.shape('slash7.gif')
    time.sleep(.05)
    slash.hideturtle()
    

    

def load_screen():
    wn.tracer(False)
    global menu_status
    menu_staus_hold = menu_status
    menu_status = 'loading'
    loader.goto(1920,1080)
    loader.pendown()
    x = loader.xcor()
    y = loader.ycor()
    wn.tracer(True)
    while (x >= -1920):
        loader.goto(x,(-1 * y))
        x = x - 60
        loader.goto(x,(-1 * y))
        loader.goto(x,y)
    menu_status = menu_staus_hold
# pain
def type_fight(fight_text):
    if menu_status == 'home':
        global current_text
        current_text = fight_text
        commentator.clear()
        commentator.write(fight_text, font=("Impact", 30, "bold"))
        time.sleep(1.5)
    else:
        useless.forward(1)
    
def save_text():
    commentator.clear()
    if (menu_status == 'home'):
        commentator.write(current_text, font=("Impact", 30, "bold"))

#updates the currency of the game, and displays it in the bottom left part of the screen
def update_bobux():
    global menu_status
    global bobux
    bobux_counter.clear()
    if (menu_status == 'home'):
        bobux_counter.write(str(bobux) + " Schmekles (press b to go to the shop)", font=("Impact", 40, "bold"))
    elif(menu_status == 'shop'):
        bobux_counter.write(str(bobux) + " Schmekles (press a to go to the main screen)", font=("Impact", 40, "bold"))

#adds a number in each box to show the user what buttons correspond to what actions
def label_number():
    a = box_1.xcor()
    b = box_2.ycor()
    c = box_2.xcor()
    d = box_2.ycor()
    e = box_3.xcor()
    f = box_3.ycor()
    g = box_4.xcor()
    h = box_4.ycor()
    box_1.goto(-690,-390)
    box_2.goto(-340,-390)
    box_3.goto(10,-390)
    box_4.goto(360,-390)
    box_1.write("1", font=("Impact", 40, "bold"))
    box_2.write("2", font=("Impact", 40, "bold"))
    box_3.write("3", font=("Impact", 40, "bold"))
    box_4.write("4", font=("Impact", 40, "bold"))
    box_1.goto(a,b)
    box_2.goto(c,d)
    box_3.goto(e,f)
    box_4.goto(g,h)

#makes the text for the bottom of the screen, using button list to allow easy changing of the bottom option texts
def bottom_text():
    box_1.clear()
    box_2.clear()
    box_3.clear()
    box_4.clear()
    player_hptxt.clear()
    gatorade_text.clear()
    ultimate_text.clear()
    enemy_hptxt.clear()
    box_1.write(button_list[0], font=("Impact", 40, "bold"))
    box_2.write(button_list[1], font=("Impact", 40, "bold"))
    box_3.write(button_list[2], font=("Impact", 40, "bold"))
    box_4.write(button_list[3], font=("Impact", 40, "bold"))
    label_number()

#makes the entire menu screen and can be used to delete/make the menu
def make_home():
    global menu_status
    global button_list
    global bobux
    if (menu_status != 'home') and (menu_status != 'loading') and (menu_status != 'commentating'):
        load_screen()
        wn.tracer(False)
        button_list = ["Fire Ball", "Heal", "Power Up", "Final Strike"]
        drawer.clear()
        fancyshaq.hideturtle()
        player.showturtle()
        enemy.showturtle()
        healthbar.showturtle()
        ultbar.showturtle()
        enemyhealthbar.showturtle()
        potionbar.showturtle()
        drawer.pu()
        drawer.goto(-700,-200)
        drawer.pendown()
        drawer.goto(700,-200)
        drawer.goto(700,-400)
        drawer.goto(-700,-400)
        drawer.goto(-700,-200)
        drawer.goto(0,-200)
        drawer.goto(0,-400)
        drawer.goto(-350,-400)
        drawer.goto(-350,-200)
        drawer.goto(350,-200)
        drawer.goto(350,-400)
        drawer.pu()
        drawer.goto(-700,-75)
        drawer.pendown()
        drawer.goto(700,-75)
        drawer.goto(700,-175)
        drawer.goto(-700,-175)
        drawer.goto(-700,-75)
        y = 0
        for i in range(3):
            drawer.pu()
            drawer.goto(-700,(200-y))
            drawer.pendown()
            drawer.goto(-300,(200-y))
            drawer.goto(-300,(150-y))
            drawer.goto(-700,(150-y))
            drawer.goto(-700,(200-y))
            y = y + 100
        drawer.pu()
        drawer.goto(-250,0)
        drawer.pendown()
        drawer.goto(650,0)
        drawer.goto(650,-50)
        drawer.goto(-250,-50)
        drawer.goto(-250,0)
        box_1.goto(-690,-330)
        box_2.goto(-340,-330)
        box_3.goto(10,-330)
        box_4.goto(360,-330)
        bottom_text()
        player_hptxt.write("HP", font=("Impact", 20, "bold"))
        gatorade_text.write("POTIONS", font=("Impact", 20, "bold"))
        ultimate_text.write("DUNK CITY", font=("Impact", 20, "bold"))
        enemy_hptxt.write("ENEMY HP", font=("Impact", 20, "bold"))
        loader.clear()
        menu_status = 'home'
        save_text()
        update_bobux()
        wn.tracer(True)

#makes the entire shop screen and can be used to delete/make the menu
def make_shop():
    global menu_status
    global button_list
    global bobux
    if (menu_status != 'shop') and (menu_status != 'loading') and (menu_status != 'commentating'):
        menu_status = 'shop'
        load_screen()
        wn.tracer(False)
        button_list = ["Potions", "Wands", "Robes", "シャキール"]
        drawer.clear()
        bottom_text()
        enemy.hideturtle()
        player.hideturtle()
        healthbar.hideturtle()
        ultbar.hideturtle()
        enemyhealthbar.hideturtle()
        potionbar.hideturtle()
        fancyshaq.showturtle()
        drawer.clear()
        drawer.pu()
        drawer.goto(-700,-200)
        drawer.pendown()
        drawer.goto(700,-200)
        drawer.goto(700,-400)
        drawer.goto(-700,-400)
        drawer.goto(-700,-200)
        drawer.goto(0,-200)
        drawer.goto(0,-400)
        drawer.goto(-350,-400)
        drawer.goto(-350,-200)
        drawer.goto(350,-200)
        drawer.goto(350,-400)
        loader.clear()
        save_text()
        update_bobux()
        wn.tracer(True)
    
#--------loop--------
make_home()
wn.onkeypress(make_home, 'a')
wn.onkeypress(make_shop, 'b')
#type_fight("Funny fart")
wn.listen()