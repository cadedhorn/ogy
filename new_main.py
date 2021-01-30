# GOD BLESS STATEFARM THANK YOU FOR MAKING THE GAME ACTUALLY WORK. HOLY JESUS CHRIST.
import turtle as jake
import winsound
import render as rn
statefarm = jake.Screen()
import new_attacks as atk
atk.setenemyfile('test.txt')
atk.setplayerfile('test.txt')
rn.player_attacks = ['this','game','sucks','lol']
rn.menu_status = 'hasdsd'
rn.make_home()
winsound.PlaySound(None,winsound.SND_ASYNC)
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