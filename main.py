# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
from playsound import playsound
statefarm = jake.Screen()
import attacks as atk
playsound('battle.mp3',block=False);
while atk.enemy_hp > 0 and atk.menu_status == 'home':
    atk.setenemyfile('ogre.txt')
    atk.setplayerfile('wizardogy.txt')
    atk.playerchoose()
statefarm.mainloop()