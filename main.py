# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
from playsound import playsound
statefarm = jake.Screen()
from attacks import *
setenemyfile('ogre.txt')
setplayerfile('aaberg.txt')
playsound('battle.mp3',block=False);
battle = True
def battlestate(x):
    global battle
    battle = x
funny = 1
while battle == True:
    playerchoose()
type_fight("lol funny fart :)))")
statefarm.mainloop()