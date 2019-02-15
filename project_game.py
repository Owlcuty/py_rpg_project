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
    print(f'hp: {hero.hp_now} / {hero.hp}')
    print(f'mp: {hero.mp_now} / {hero.mp}')
    print(f'stamina: {hero.stam_now} / {hero.stam}')
    print(f'strength: {hero.strength}')
    print(f'agility: {hero.agility}')
    print(f'intelligence: {hero.intelligence}')
    print(f'sense: {hero.sense}')
    print(f'vitality: {hero.vitality}')
    print(f'effect_fis: {hero.effect_fis}')
    print(f'effect_mag: {hero.effect_mag}')
    print()
    print(f'attack: {hero.attack}')
    print()
    print(f'length of step: {hero.step}')
    print()
    print(f'add_points: {hero.add_points}')
    print()


def upgrade():
    global hero
    while hero.add_points > 0:
        print(
            f'You have {hero.add_points} points for upgrade your characterizations. If you want to exit write "cancel"')
        print('Choose stat:')
        print(f'1.    strength: {hero.strength}')
        print(f'2.    intelligence: {hero.intelligence}')
        print(f'3.    sense: {hero.sense}')
        print(f'4.    vitality: {hero.vitality}')
        stat = input()
        if stat == "cancel":
            break
        if len(stat.split()) != 2 or (
                len(stat.split()) == 2 and not (stat.split()[0].isdigit() and stat.split()[1].isdigit())):
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
        hero = hero.up(hero)


def attack():
    while True:
        try:
            attacked_enemy = input("Choose coordinates of enemy's unit like \"H5\" or write cancel\n")
            if attacked_enemy == 'cancel':
                return
            attacked_enemy = [abc.index(attacked_enemy[0])] + [int(attacked_enemy[1:]) - 1]
            for it in lvls[level].units.keys():
                if not it in ['Hero', 'Exit', 'Trap', 'Poison']:
                    for xy in lvls[level].units[it]:
                        if xy.y == attacked_enemy[0] and xy.x == attacked_enemy[1]:
                            if hero.attack_radius == 1:
                                if abs(xy.y - hero.y) + abs(xy.x - hero.x) <= 2:
                                    xy = hero.attack_enemy(xy, hero.attack)
                                    return
                            else:
                                if abs(xy.x - hero.x) <= hero.attack_radius and abs(
                                        xy.y - hero.y) <= hero.attack_radius and not (
                                        abs(xy.x - hero.x) == hero.attack_radius and abs(xy.y - hero.y) == hero.attack_radius):
                                    xy = hero.attack_enemy(xy, hero.attack)
                                    return
        except:
            print(f'Pls, write correct coordinates. There is nobody on {attacked_enemy}')


sh_stat = True


def execute_command(command):
    global sh_stat
    com = {
        'show status': show_status,
        'exit': exit,
        'go': lvls[level].go,
        'attack': attack,
        'upgrade': upgrade,
        'show map': draw_map
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
        sh_stat = True
        lvls[level].check_for_enemy()
    else:
        sh_stat = False


def check_enemies():
    for it in lvls[level].units.keys():
        if not it in ['Hero', 'Exit', 'Trap', 'Poison']:
            for i in range(len(lvls[level].units[it])):
                if i >= len(lvls[level].units[it]):
                    break
                xy = lvls[level].units[it][i]
                if xy.hp <= 0:
                    lvls[level].units[it].pop(i)


def main():
    lvls.append(lvls_names[0](Map(10, 10)))
    mp_start = choices[class_of_hero].mp_start
    stam_start = choices[class_of_hero].stam_start
    while True:
        check_enemies()
        if sh_stat:
            draw_map()
        print('_' * 50 + '\n')
        print(f'HP: {hero.hp_now} / {hero.hp}')
        if mp_start > 0:
           print('-' * 50)
           print(f'MP: {hero.mp_now} / {hero.mp}')
        if stam_start > 0:
           print('-' * 50)
           print(f'Stamina: {hero.stam_now} / {hero.stam}')
        print('-' * 50)
        print('Level: ', hero.lvl, f' {hero.max_of_level[0]}/{hero.max_of_level[1]}')
        print('_' * 50)
        if hero.add_points > 0:
            print(f'You have {hero.add_points} points for upgrade your characterizations')

        execute_command(input('Choose your step: (show status, go, attack, exit, upgrade (stats), show map\n'))
        hero.hp_now += min(5, hero.hp - hero.hp_now)


if __name__ == '__main__':
    main()
