# demo / testbed for new attack framework (old one won't work for more ambitious ideas)

import turtle as trtl
fireball = trtl.Turtle()
wn = trtl.Screen()
fireball.shape('circle')
fireball.color('red')
fireball.hideturtle()
enemy_hp = 10
player_hp = 10
enemy_pwr = 2
player_pwr = 2

def fireball_animation():
    fireball.showturtle()
    fireball.forward(40)
    fireball.hideturtle()

def fireball_attack():
    global enemy_hp, player_pwr
    enemy_hp = enemy_hp - player_pwr
    fireball_animation()
    print(enemy_hp)

with open('test.txt','r') as file:
    stats = file.readlines()
eval(stats[0])
wn.mainloop()