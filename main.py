# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
from playsound import playsound
statefarm = jake.Screen()
from attacks import *
setenemyfile('ogre.txt')
setplayerfile('gipe.txt')
playsound('battle.mp3',block=False);
while enemy_hp > 0 and menu_status == 'home':
    playerchoose()
statefarm.mainloop()