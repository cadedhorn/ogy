# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
from playsound import playsound
statefarm = jake.Screen()
import attacks as atk
atk.setenemyfile('ogre.txt')
atk.setplayerfile('wizardogy.txt')
playsound('battle.mp3',block=True);
while atk.enemy_hp > 0 and atk.menu_status == 'home':
    atk.playerchoose()
statefarm.mainloop()