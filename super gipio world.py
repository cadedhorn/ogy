import turtle as funny
gamemap = funny.Turtle()
useless = funny.Turtle()
useless.pu()
useless.hideturtle()
jonas = funny.Turtle()
wn = funny.Screen()
wn.tracer(False)
k = 90
steps = 0
gamemap.up()
gamemap.seth(k)
wn.addshape('stick.gif')
wn.addshape('stickleft1.gif')
wn.addshape('stickleft2.gif')
wn.addshape('testbg.gif')
gamemap.shape('testbg.gif')
fun = 'stick.gif'
jonas.shape(fun)
wn.tracer(True)
def uselesslol():
    useless.forward(1)
def lol():
    gamemap.back(10)
def goforward():
    global k, steps, fun
    if steps % 8 in range(0,5):
        if fun != 'stickleft1.gif':
            fun = 'stickleft1.gif'
            jonas.shape(fun)
    elif steps % 8 in range(4,9):
        if fun != 'stickleft2.gif':
            fun = 'stickleft2.gif'
            jonas.shape(fun)
    if k != 90:
        k = 90
        gamemap.seth(k)
    if gamemap.ycor() > -540+145:
        lol()
        steps += 1
def goback():
    global k, steps, fun
    if steps % 8 in range(0,5):
        if fun != 'stickleft1.gif':
            fun = 'stickleft1.gif'
            jonas.shape(fun)
    elif steps % 8 in range(4,9):
        if fun != 'stickleft2.gif':
            fun = 'stickleft2.gif'
            jonas.shape(fun)
    if k != 270:
        k = 270
        gamemap.seth(k)
    if gamemap.ycor() < 540-145:
        lol()
        steps += 1
def goright():
    global k, steps, fun
    if steps % 8 in range(0,5):
        if fun != 'stickleft1.gif':
            fun = 'stickleft1.gif'
            jonas.shape(fun)
    elif steps % 8 in range(4,9):
        if fun != 'stickleft2.gif':
            fun = 'stickleft2.gif'
            jonas.shape(fun)
    if k != 0:
        k = 0
        gamemap.seth(k)
    if gamemap.xcor() > -960+145:
        lol()
        steps += 1
def goleft():
    global k, steps, fun
    if steps % 8 in range(0,5):
        if fun != 'stickleft1.gif':
            fun = 'stickleft1.gif'
            jonas.shape(fun)
    elif steps % 8 in range(4,9):
        if fun != 'stickleft2.gif':
            fun = 'stickleft2.gif'
            jonas.shape(fun)
    if k != 180:
        k = 180
        gamemap.seth(k)
    if gamemap.xcor() < 960-145:
        lol()
        steps += 1
def resetimage():
    jonas.shape('stick.gif')
    steps = 0
wn.onkeypress(goforward,"w")
wn.onkeypress(goleft,"a")
wn.onkeypress(goback,"s")
wn.onkeypress(goright,"d")
wn.onkeyrelease(resetimage,"w")
wn.onkeyrelease(resetimage,"a")
wn.onkeyrelease(resetimage,"s")
wn.onkeyrelease(resetimage,"d")
wn.listen()
wn.mainloop()
