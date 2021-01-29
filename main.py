# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
from playsound import playsound
statefarm = jake.Screen()
from attacks import *
setenemyfile('ogre.txt')
setplayerfile('gipe.txt')
playsound('battle.mp3',block=False);
battle = True
while battle == True:
    playerchoose()
type_fight("owned")
statefarm.mainloop()