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
wn.tracer(True)

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

# box_1.hideturtle()
# box_2.hideturtle()
# box_3.hideturtle()
# box_4.hideturtle()

global menu_status
menu_status = 'placeholder'

#--------Functions--------

def make_home():
    global menu_status
    if (menu_status != 'home'):
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
        menu_status = 'home'

def make_shop():
    global menu_status
    if (menu_status != 'shop'):
        drawer.clear()
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
        menu_status = 'shop'
    
def bottom_text():
    box_1.hideturtle()
    box_2.hideturtle()
    box_3.hideturtle()
    box_4.hideturtle()
    box_1.goto(-668,-330)
    box_2.goto(-285,-330)
    box_3.goto(100,-330)
    box_4.goto(390,-330)
    box_1.write("Free Throw", font=("Arial", 40, "bold"))
    box_2.write("Drink Up", font=("Arial", 40, "bold"))
    box_3.write("Dance", font=("Arial", 40, "bold"))
    box_4.write("Final Dunk", font=("Arial", 40, "bold"))

#--------loop--------

make_home()
bottom_text()

wn.onkeypress(make_home, 'a')
wn.onkeypress(make_shop, 'b')

wn.listen()
wn.mainloop()