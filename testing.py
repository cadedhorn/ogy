from playsound import playsound

# now change the 2nd line, note that you have to add a newline

# and write everything back
def setenemyfile(x):
    global enemy_name, enemy_hp, enemy_spe, enemy_pwr
    with open(x, 'r') as file:
        stats = file.readlines()
    enemy_name = str(stats[0]).rstrip('\n')
    enemy_hp = int(stats[1])
    enemy_spe = int(stats[2])
    enemy_pwr = int(stats[3])
setenemyfile('player.txt')
print(enemy_name + ' appeared!')
print('HP: ' + str(enemy_hp))
print('SPEED: ' + str(enemy_spe))
print('POWER: ' + str(enemy_pwr))
playsound('freeze.mp3')
    
