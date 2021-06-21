import random
from engine import engine
import operator

player = {
    'name': ['placeholder'],
    'age': ['teen','young-adult','adult','senior'],
    #'nation': ['albihelm','northelm','francia','helvetica','foma','gorma','asiago-west','asiago-east','manticolo','hispanicolo','lower-aegyptus','upper-aegpytus','bahir','sorantine'],
    'nation': ['albihelm','northelm','franchelm','asiago-west','asiago-east','manticolo-islands','hispanicolo','aegpytus','bahir','sorantine'],
    'hair-color': ['white','ginger','blonde','auburn','brown','black','grey'],
    'hair-style': ['shaved','buzz-cut','fade','spiky','side-parted','fade-back','short-loose','center-parted','medium-straight','dreadlocks','long-straight'],
    'height': ['very-short (150-160)','short (160-170)','medium (170-180)','tall (180-190)','very-tall (190-200+)'],
    'physique': ['thin','average','fat','athletic','jacked'],
    'combat-experience': ['no-experience','novice','trained','expert','master','super-human'],
    'enemy-type': ['swordsman','spearman','archer','rifleman','guard','knight'],
    'health': [1,2,3,4,5,6],
    'strength': [1,2,3,4,5,6],
    'endurance': [1,2,3,4,5,6],
    'dexterity': [1,2,3,4,5,6],
    'movement': [1,2,3,4,5,6],
    'money': [0]
}

enemy = {
    'name': ['placeholder'],
    'age': ['teen','young-adult','adult','senior'],
    'nation': ['albihelm','northelm','franchelm','asiago-west','asiago-east','manticolo-islands','hispanicolo','aegpytus','bahir','sorantine'],
    'hair-color': ['white','ginger','blonde','auburn','brown','black','grey'],
    'hair-style': ['shaved','buzz-cut','fade','spiky','side-parted','fade-back','short-loose','center-parted','medium-straight','dreadlocks','long-straight'],
    'height': ['very-short (150-160)','short (160-170)','medium (170-180)','tall (180-190)','very-tall (190-200+)'],
    'physique': ['thin','average','fat','athletic','jacked'],
    'combat-experience': ['no-experience','novice','trained','expert','master','super-human'],
    'enemy-type': ['swordsman','spearman','archer','rifleman','guard','knight'],
    'health': [1,2,3,4,5,6],
    'strength': [1,2,3,4,5,6],
    'endurance': [1,2,3,4,5,6],
    'dexterity': [1,2,3,4,5,6],
    'movement': [1,2,3,4,5,6],
    'money': [0]
    }

attack_types=['strength','endurance','dexterity','movement']

def player_init():
    engine.create(player,'player')
    player_output=engine.generate(player)
    player_output['name']=engine.mname()
    player_output['money']=random.randint(0, 5)
    engine.update(player_output,'player')

def enemy_init():
    engine.create(enemy,'enemy')
    enemy_output=engine.generate(enemy)
    enemy_output['name']=engine.mname()
    enemy_output['money']=random.randint(0, 5)
    engine.update(enemy_output,'enemy')

def play():
    player_init()
    player_char=engine.retrieve('player')
    enemy_init()
    enemy_char=engine.retrieve('enemy')

    sel = ''
    while (sel != 'q' and 'quit'):
        sel = input('\nchoose where to go, adventurer: ')

        if sel == 'fight':
            combat(player_char, enemy_char)

        elif sel == 'stat':
            stat(player_char)

        elif sel == 'spot':
            stat(enemy_char)

        elif sel == 'shop':
            shop()

        elif sel == 'train':
            player_char=train(player_char)

        elif sel == 'gear':
            gear()

        elif sel == 'heal':
            player_char=heal(player_char)

        elif sel == 'wait':
            enemy_char=wait()

def stat(char):
    print('stat here')
    print(char)

def shop():
    print('shop here')

def train(player_char):
    print('train here')
    r1 = random.randint(0, len(attack_types)-1)
    r2 = random.randint(-1, 2)
    player_char[attack_types[r1]] = player_char[attack_types[r1]] + r2
    print(player_char['name'] + ' tweaked ' + attack_types[r1] + ' by ' + str(r2))
    return player_char

def gear():
    print('gear here')

def heal(player_char):
    player_char['health']=player_char['health']+1
    player_char['money']=player_char['money']-1
    return player_char

def wait():
    enemy_char=enemy_init()
    return enemy_char

def combat(player_char, enemy_char):
    winner = -1
    turn = 1

    player_attacks=[]
    enemy_attacks=[]

    player_attacks.append(player_char['strength'])
    player_attacks.append(player_char['endurance'])
    player_attacks.append(player_char['dexterity'])

    enemy_attacks.append(enemy_char['strength'])
    enemy_attacks.append(enemy_char['endurance'])
    enemy_attacks.append(enemy_char['dexterity'])

    player_highest_attack_index, player_highest_attack_value = max(enumerate(player_attacks), key=operator.itemgetter(1))
    enemy_highest_attack_index, enemy_highest_attack_value = max(enumerate(enemy_attacks), key=operator.itemgetter(1))

    if player_char['movement'] > enemy_char['movement']:
        turn = 1
        print('the player went first with ' + str(player_char['movement']) + ' over ' + str(enemy_char['movement']))
    else:
        turn = 2
        print('the enemy went first with ' + str(enemy_char['movement']) + ' over ' + str(player_char['movement']))

    while(winner == -1):
        if turn % 2 == 1:
            enemy_char['health']=enemy_char['health']-player_attacks[player_highest_attack_index]
            print(player_char['name'] + ' used his ' + str(attack_types[player_highest_attack_index]) + ' to deal ' + str(player_highest_attack_value) + ' damage')
        else:
            player_char['health']=player_char['health']-enemy_attacks[enemy_highest_attack_index]
            print(enemy_char['name'] + ' used his ' + str(attack_types[enemy_highest_attack_index]) + ' to deal ' + str(enemy_highest_attack_value) + ' damage')
        if(player_char['health'] <= 0):
            winner = 0
            print('the player lost')
        elif(enemy_char['health'] <= 0):
            winner = 1
            player_char['money'] = player_char['money'] + enemy_char['money']
            print('the player won and gained ' + str(enemy_char['money']) + ' money')
            enemy_char=enemy_init()
        turn = turn + 1
