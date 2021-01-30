# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
import winsound
statefarm = jake.Screen()
import attacks as atk
atk.setenemyfile('ogre.txt')
atk.setplayerfile('wizardogy.txt')
winsound.PlaySound('souljaboy.wav',winsound.SND_ASYNC)
while atk.menu_status != 'end_fight':
    atk.playerchoose()
winsound.PlaySound(None,winsound.SND_PURGE)
atk.setenemyfile('aaberg.txt')
winsound.PlaySound('aaberg.wav',winsound.SND_ASYNC)
atk.menu_status = 'home'
while atk.menu_status != 'end_fight':
    atk.playerchoose()
atk.type_fight("lol funny fart :)))")
winsound.PlaySound(None,winsound.SND_PURGE)
statefarm.mainloop()