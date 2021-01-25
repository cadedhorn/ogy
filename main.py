import turtle as trtl
import random

#--------Setup--------

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

drawer = trtl.Turtle()
drawer.pensize(5)
drawer.speed(0)

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
make_shop()

wn.listen()
wn.mainloop()