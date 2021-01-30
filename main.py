# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
from playsound import playsound
statefarm = jake.Screen()
import attacks as atk
atk.setenemyfile('ogre.txt')
atk.setplayerfile('aaberg.txt')
playsound('aaberg.mp3',block=False);

while atk.menu_status != 'end_fight':
    atk.playerchoose()
atk.setenemyfile('wizardogy.txt')
atk.menu_status = 'home'
while atk.menu_status != 'end_fight':
    atk.playerchoose()
atk.type_fight("lol funny fart :)))")
statefarm.mainloop()