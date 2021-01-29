import turtle
funny = turtle.Turtle()
wn = turtle.Screen()
with open('test.txt','r') as file:
    stats = file.readlines()
eval(stats[0])
wn.mainloop()