RULES = '''

hp
mp
lvl
strength
agility
intelligence
sense
vitality
effect

hp_start, mp_start, strength_start, agility_start, intelligence_start, sense_start, vitality_start

'''
import math
from Action import *
from class_objects import choices

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


def show_status():
    # TODO show the hero's characterizations
    print('Status of hero')
    print('_' * 50)
    print(f'level: {hero.lvl}')
    print(f'hp: {hero.hp}')
    print(f'mp: {hero.mp}')
    print(f'stamina: {hero.stam}')
    print(f'strength: {hero.strength}')
    print(f'intelligence: {hero.intelligence}')
    print(f'sense: {hero.sense}')
    print(f'vitality: {hero.vitality}')
    print(f'effect_fis: {hero.effect_fis}')
    print(f'effect_mag: {hero.effect_mag}')
    print(f'length of step: {hero.step}')
    print()
    print(f'add_points: {hero.add_points}')
    print()


def upgrade():
    while hero.add_points > 0:
        print(f'You have {hero.add_points} points for upgrade your characterizations. If you want to exit write "cancel"')
        print('Choose stat:')
        print(f'1.    strength: {hero.strength}')
        print(f'2.    intelligence: {hero.intelligence}')
        print(f'3.    sense: {hero.sense}')
        print(f'4.    vitality: {hero.vitality}')
        stat = input()
        if stat == "cancel":
            break
        if len(stat.split()) != 2 or (len(stat.split()) == 2 and not (stat.split()[0].isdigit() and stat.split()[1].isdigit())):
            print("Pls, write correct like '1 5' ( to upgrade strength on 5 points )")
            continue
        stat = stat.split()
        while stat[0] != "cancel" and int(stat[1]) > hero.add_points:
            print("You don't have so many points. Please, choose again")
            stat = input('Stat and number of points or write "cancel"\n').split()
        if stat[0] == '1':
            hero.strength += int(stat[1])
        elif stat[0] == '2':
            hero.intelligence += int(stat[1])
        elif stat[0] == '3':
            hero.sense += int(stat[1])
        elif stat[0] == '4':
            hero.vitality += int(stat[1])
        hero.add_points -= int(stat[1])
        uni = hero.up(hero)
        hero.hp = uni.hp
        hero.mp = uni.mp
        hero.stam = uni.stam


def execute_command(command):
    com = {
        'show status': show_status,
        'exit': exit,
        'go': lvls[level].go,
        'attack': 1,
        'upgrade': upgrade
    }
    if command == 'go':
        com[command](hero)
    elif command in com.keys():
        com[command]()
    else:
        print('Please, write correct command:')
        print('\t show status')
        print('\t exit')
        print('\t go')
        print('\t attack')
        print('\t upgrade (stats)')
        execute_command(input())
    if command != 'show status':
        lvls[level].check_for_enemy()


def main():
    lvls.append(lvls_names[0](Map(10, 10)))
    while True:
        draw_map()
        print('_'*50+'\n')
        print('HP: ', hero.hp)
        print('-'*50)
        print('MP: ', hero.mp)
        print('-'*50)
        print('Stamina: ', hero.stam)
        print('_'*50)
        if hero.add_points > 0:
            print(f'You have {hero.add_points} points for upgrade your characterizations')

        execute_command(input('Choose your step: (show status, go, attack, exit, upgrade (stats)\n'))


if __name__ == '__main__':
    main()
