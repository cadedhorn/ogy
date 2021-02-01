# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
import winsound
statefarm = jake.Screen()
import attacks as atk
#SETS UP FIRST FIGHT
atk.setenemyfile('ogre.txt')
atk.setplayerfile('wizardogy.txt')
winsound.PlaySound('aaberg.wav',winsound.SND_ASYNC)

#SETS UP FIGHT FIGHT
while atk.menu_status != 'end_fight':
    atk.playerchoose()
winsound.PlaySound(None,winsound.SND_PURGE)
atk.menu_status = 'home'

#CHECKS TO SEE IF DEAD
if (atk.player_hp > 0):
    atk.setenemyfile('aaberg.txt')
    winsound.PlaySound('aaberg.wav',winsound.SND_ASYNC)

#FIGHT PART 2 ELECTRIC BOOGALOO
while atk.menu_status != 'end_fight':
    atk.playerchoose()
atk.type_fight("lol funny fart :)))")
winsound.PlaySound(None,winsound.SND_PURGE)
statefarm.mainloop()
