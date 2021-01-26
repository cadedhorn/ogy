import turtle as trtl
import random

#--------Setup--------

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape('beetlehand.gif')
wn.addshape('neutralshaq.gif')
wn.addshape('fancyshaq.gif')

wn.tracer(False)
enemy = trtl.Turtle()
enemy.hideturtle()
enemy.shape('beetlehand.gif')
enemy.pu()
enemy.goto(200,245)

neutralshaq = trtl.Turtle()
neutralshaq.hideturtle()
neutralshaq.shape('neutralshaq.gif')
neutralshaq.pu()
neutralshaq.goto(-500,375)

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

shaq_hp = trtl.Turtle()
gatorade_text = trtl.Turtle()
ultimate_text = trtl.Turtle()
enemy_hp = trtl.Turtle()

shaq_hp.hideturtle()
gatorade_text.hideturtle()
ultimate_text.hideturtle()
enemy_hp.hideturtle()

shaq_hp.pu()
gatorade_text.pu()
ultimate_text.pu()
enemy_hp.pu()

shaq_hp.speed(0)
gatorade_text.speed(0)
ultimate_text.speed(0)
enemy_hp.speed(0)

shaq_hp.goto(-700,200)
gatorade_text.goto(-700,100)
ultimate_text.goto(-700,0)
enemy_hp.goto(-250,0)

bobux_counter = trtl.Turtle()
bobux_counter.pu()
bobux_counter.hideturtle()
bobux_counter.goto(-700,-475)

bobux = 0
wn.tracer(True)

global menu_status
menu_status = 'placeholder'

global button_list
button_list = []
#--------Functions--------

def update_bobux():
    bobux_counter.clear()
    bobux_counter.write(bobux, font=("Arial", 40, "bold"))

def label_number():
    a = box_1.xcor()
    b = box_2.ycor()
    c = box_2.xcor()
    d = box_2.ycor()
    e = box_3.xcor()
    f = box_3.ycor()
    g = box_4.xcor()
    h = box_4.ycor()
    box_1.goto(-530,-390)
    box_2.goto(-180,-390)
    box_3.goto(170,-390)
    box_4.goto(520,-390)
    box_1.write("1", font=("Arial", 40, "bold"))
    box_2.write("2", font=("Arial", 40, "bold"))
    box_3.write("3", font=("Arial", 40, "bold"))
    box_4.write("4", font=("Arial", 40, "bold"))
    box_1.goto(a,b)
    box_2.goto(c,d)
    box_3.goto(e,f)
    box_4.goto(g,h)

def bottom_text():
    box_1.clear()
    box_2.clear()
    box_3.clear()
    box_4.clear()
    shaq_hp.clear()
    gatorade_text.clear()
    ultimate_text.clear()
    enemy_hp.clear()
    box_1.write(button_list[0], font=("Arial", 40, "bold"))
    box_2.write(button_list[1], font=("Arial", 40, "bold"))
    box_3.write(button_list[2], font=("Arial", 40, "bold"))
    box_4.write(button_list[3], font=("Arial", 40, "bold"))
    label_number()
    


def make_home():
    global menu_status
    global button_list
    if (menu_status != 'home'):
        wn.tracer(False)
        button_list = ["Free Throw", "Drink Up", "Dance", "Final Dunk"]
        drawer.clear()
        fancyshaq.hideturtle()
        neutralshaq.showturtle()
        enemy.showturtle()
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
        box_1.goto(-668,-330)
        box_2.goto(-285,-330)
        box_3.goto(100,-330)
        box_4.goto(390,-330)
        bottom_text()
        shaq_hp.write("HP", font=("Arial", 20, "bold"))
        gatorade_text.write("GATORADE", font=("Arial", 20, "bold"))
        ultimate_text.write("DUNK CITY", font=("Arial", 20, "bold"))
        enemy_hp.write("ENEMY HP", font=("Arial", 20, "bold"))
        update_bobux()
        menu_status = 'home'
        wn.tracer(True)

def make_shop():
    global menu_status
    global button_list
    if (menu_status != 'shop'):
        wn.tracer(False)
        button_list = ["Gatorade", "Basquetbol", "Uni-Forme", "シャキール"]
        drawer.clear()
        box_1.goto(-635,-330)
        box_2.goto(-315,-330)
        box_3.goto(43,-330)
        box_4.goto(390,-330)
        bottom_text()
        enemy.hideturtle()
        neutralshaq.hideturtle()
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
        update_bobux()
        menu_status = 'shop'
        wn.tracer(True)
    
#--------loop--------
make_home()

wn.onkeypress(make_home, 'a')
wn.onkeypress(make_shop, 'b')

wn.listen()
wn.mainloop()