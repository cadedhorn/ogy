import turtle as trtl
import random
# ur gay lol
#--------Setup--------

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape('beetlehand.gif')
wn.addshape('neutralshaq.gif')
wn.addshape('madface.gif')

enemy = trtl.Turtle()
enemy.shape('beetlehand.gif')
enemy.pu()
enemy.goto(200,145)

goodguy = trtl.Turtle()
goodguy.shape('neutralshaq.gif')
goodguy.pu()
goodguy.goto(-500,375)

drawer = trtl.Turtle()
drawer.pensize(5)
drawer.speed(0)
drawer.hideturtle()

box_1 = trtl.Turtle()
box_2 = trtl.Turtle()
box_3 = trtl.Turtle()
box_4 = trtl.Turtle()
#--------Functions--------

def make_home():
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
    drawer.goto(-300,-100)
    drawer.pendown()
    drawer.goto(700,-100)
    drawer.goto(700,-150)
    drawer.goto(-300,-150)
    drawer.goto(-300,-100)

def make_shop():
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
#--------loop--------
make_home()

wn.listen()
wn.mainloop()