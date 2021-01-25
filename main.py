import turtle as trtl
import random

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

drawer = trtl.Turtle()
drawer.pensize(5)

def make_home():
    drawer.penup()
    drawer.goto(-600,-200)
    drawer.pendown()
    drawer.goto(600,-200)
    drawer.goto(600,-400)
    drawer.goto(-600,-400)
    drawer.goto(-600,-200)
    drawer.penup

make_home()






wn.listen()
wn.mainloop()
