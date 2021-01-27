import turtle as trtl
commentator = trtl.Turtle()
commentator.hideturtle()
commentator.pu()
commentator.goto(-100,-100)
commentator.speed()
wn = trtl.Screen()

#functions
#types the ACTION
def type_fight(fight_text):
    commentator.write(fight_text, font=("Arial", 20, "bold"))
type_fight("LOL")
wn.mainloop()