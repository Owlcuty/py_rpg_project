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
import random
import math

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


# from colorama import init, Fore, Back, Style

class Unit(object):
    hp = None
    mp = None
    stam = None


class Warrior(object):
    '''
        description of unit's class
    '''
    hp_start = 100
    mp_start = 30
    stam_start = 60
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit
        uni.hp = player.hp + player.strength * 3 + player.vitality * 2 + player.agility - player.intelligence
        uni.mp = player.mp + math.floor(player.intelligence * 1.5) + player.sense
        uni.stam = player.stam + player.vitality * 2.5 + player.intelligence - player.agility + player.strength * 1.5
        return uni


class Palladin(object):
    '''
        description of unit's class
    '''
    hp_start = 150
    mp_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit
        uni.hp = player.hp + player.strength * 3 + player.vitality * 2 + player.agility - player.intelligence
        uni.mp = math.floor(player.intelligence * 1.5) + player.sense
        uni.stam = player.vitality * 2.5 + player.intelligence - player.agility + player.strength * 1.5
        return uni


class Magician(object):
    '''
        description of unit's class
    '''
    hp_start = 100
    mp_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit
        uni.hp = player.hp + player.strength * 3 + player.vitality * 2 + player.agility - player.intelligence
        uni.mp = math.floor(player.intelligence * 1.5) + player.sense
        uni.stam = player.vitality * 2.5 + player.intelligence - player.agility + player.strength * 1.5
        return uni


class Slayer(object):
    '''
        description of unit's class
    '''
    hp_start = 100
    mp_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit
        uni.hp = player.hp + player.strength * 3 + player.vitality * 2 + player.agility - player.intelligence
        uni.mp = math.floor(player.intelligence * 1.5) + player.sense
        uni.stam = player.vitality * 2.5 + player.intelligence - player.agility + player.strength * 1.5
        return uni


class Prophet(object):
    '''
        description of unit's class
    '''
    hp_start = 100
    mp_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8

    @staticmethod
    def up(player):
        '''

            :param player: unit's object (class) (hero/enemy)
            :return: unit's object
        '''
        uni = Unit
        uni.hp = player.hp + player.strength * 3 + player.vitality * 2 + player.agility - player.intelligence
        uni.mp = math.floor(player.intelligence * 1.5) + player.sense
        uni.stam = player.vitality * 2.5 + player.intelligence - player.agility + player.strength * 1.5
        return uni


name_of_classes = {
    'Warrior': 'war',
    'Magician': 'mag',
    'Prophet': 'pro',
    'Paladin': 'pal',
    'Slayer': 'slr'
}
choices = {
    # TODO selected class's object by name
    'war': Warrior,
    'mag': Magician,
    'pal': Palladin,
    'pro': Prophet,
    'slr': Slayer
}


class Class(object):
    '''
        description of any unit with selected here class with initial characterizations
    '''
    hp_start = None
    mp_start = None
    strength_start = None
    agility_start = None
    intelligence_start = None
    sense_start = None
    vitality_start = None
    up = lambda: True
    unit = None

    def __init__(self, choice):
        '''

        :param choice: class name
        '''
        # TODO selecting unit's class
        self.unit = choices[choice]
        self.up = self.unit.up



class Hero(Class):
    '''
        Hero's characterizations with their refreshing
    '''
    hp = None
    mp = None
    stam = None
    lvl = None
    attack = None
    strength = None
    agility = None
    intelligence = None
    sense = None
    vitality = None
    effect_fis = 0
    effect_mag = 0
    x = None
    y = None
    add_points = 5

    def set_start_datas(self):
        self.hp = self.unit.hp_start
        self.mp = self.unit.mp_start
        self.stam = self.unit.stam_start
        self.strength = self.unit.strength_start
        self.agility = self.unit.agility_start
        self.intelligence = self.unit.intelligence_start
        self.sense = self.unit.sense_start
        self.vitality = self.unit.vitality_start
        self.lvl = 0

    def take_damage(self, damage):
        '''

        :param damage: damage taken from enemy or posion/trap
        '''
        # TODO damage definition | die of hero
        self.hp -= damage
        if self.hp <= 0:
            print("DIIIIE, sorry =)")
            exit(0)

    def refresh(self):
        # TODO refreshing characterizations
        uni = self.unit.up(self.hp, self.mp, self.stam)
        self.hp = uni.hp
        self.mp = uni.mp
        self.stam = uni.stam


class Enemy(Class):
    '''
        Enemy's characterizations with their refreshing
    '''
    hp = None
    mp = None
    stam = None
    lvl = None
    attack = None
    strength = None
    agility = None
    intelligence = None
    sense = None
    vitality = None
    effect_fis = 0
    effect_mag = 0
    x = None
    y = None

    def _init_(self):
        self.hp = self.unit.hp_start
        self.mp = self.unit.mp_start
        self.strength = self.unit.strength_start
        self.agility = self.unit.agility_start
        self.intelligence = self.unit.intelligence_start
        self.sense = self.unit.sense_start
        self.vitality = self.unit.vitality_start

    def take_damage(self, damage):
        '''

        :param damage: damage taken from hero

        '''
        self.hp -= damage
        if self.hp <= 0:
            print("DIIIIE, sorry =)")
            exit(0)


class Map(object):
    '''
        General visible map
    '''
    n = None
    m = None
    units = {}
    maze = None

    def __init__(self, n, m):
        '''

        :param n: hight of map
        :param m: weight of map
        '''
        # TODO filling map by empty fields
        self.n, self.m = n, m
        self.maze = [['.'] * m for i in range(n)]


class Actions(object):
    '''
        General actions
    '''
    n = None
    m = None
    maze = None
    units = None
    exits = []
    mags = []
    wars = []
    pals = []
    prophs = []
    slayers = []

    def __init__(self):
        pass

    def filling(self):
        # TODO filling the map and adding new enemy's objects, hero's object and exits
        self.exits = self.units['Exit']
        hero.x, hero.y = self.units['Hero'][0][1], self.units['Hero'][0][0]

        for it in self.units.keys():
            if it in choices.keys():
                for i in range(len(self.units[it])):
                    print(self.units[it])
                    y, x = self.units[it][i][0], self.units[it][i][1]
                    self.units[it][i] = Enemy(it)
                    self.units[it][i].y, self.units[it][i].x = y, x

        print(self.units)
        for it in self.units.keys():
            if len(self.units[it]) > 0:
                for xy in self.units[it]:
                    print(it, self.units[it], xy)
                    if it in choices.keys():
                        self.maze[xy.y][xy.x] = it[0]
                    elif it == 'Hero':
                        self.maze[hero.y][hero.x] = 'H'
                        break
                    elif it == 'Exit':
                        self.maze[xy[0]][xy[1]] = it[0]
        print('_' * self.m)

    @staticmethod
    def go(unit, xy):
        # TODO displacement of unit to point (x, y)
        unit.x = int(xy[1]) - 1
        unit.y = abc.index(xy[0])
        return unit


class Lvl0(Actions):
    '''
        description of lvl1
    '''

    def __init__(self, mapp):
        # TODO filling datas about lvl
        self.n = mapp.n
        self.m = mapp.m
        self.maze = mapp.maze
        self.units = {
            'Exit': [[0, self.m - 1]],
            'Hero': [[self.n - 1, 0]],
            'mag': [[2, 5], [2, 6], [3, 7]],
            'war': [[3, 4], [4, 5], [8, 5], [6, 7]],
            'pal': [[6, 8]],
            'pro': [],
            'slr': []
        }
        self.filling()


def draw_map(self):
    # TODO drawing map
    '''

    :param self: level's object
    :return: drawn map
    '''
    for i in range(self.n):
        for j in range(self.m):
            self.maze[i][j] = '.'
    for it in self.units.keys():
        if len(self.units[it]) > 0:
            for xy in self.units[it]:
                if it in choices.keys():
                    self.maze[xy.y][xy.x] = it[0]
                elif it == 'Hero':
                    self.maze[hero.y][hero.x] = 'H'
                    break
                elif it == 'Exit':
                    self.maze[xy[0]][xy[1]] = it[0]
    print(' ', str([int(i) for i in range(1, lvls[level].m + 1)])[1:-1].split(', '))
    print('-' * (lvls[level].m * 5))
    for i in range(len(lvls[level].maze)):
        print(abc[i], lvls[level].maze[i])
    print('-' * (lvls[level].m * 5))


def show_status():
    # TODO show the hero's characterizations
    '''
    hp
    mp
    lvl
    strength
    agility
    intelligence
    sense
    vitality
    effect
    :return:
    '''
    print('Status of hero')
    print('_'*50)
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
    print()
    print(f'add_points: {hero.add_points}')
    print()


#class_of_hero = input('Please, choose your class: Warrior, Prophet, Magician, Slayer, Paladin\n')
class_of_hero = 'war'
hero = Hero(class_of_hero)
hero.set_start_datas()
lvls = [Lvl0(Map(10, 10))]
level = 0


def execute_command(command):
    if command == 'show status':
        show_status()
    if command == 'exit':
        exit()
    if command == 'go':
        lvls[level].go()


def main():
    draw_map(lvls[level])
    while True:
        draw_map(lvls[level])
        while hero.add_points > 0:
            if input(f'You have {hero.add_points} points for upgrade your characterizations. Would you want to do it? '
                     f'(yes/no)\n') == 'yes':
                print('Choose stat:')
                print(f'1.    strength: {hero.strength}')
                print(f'2.    intelligence: {hero.intelligence}')
                print(f'3.    sense: {hero.sense}')
                print(f'4.    vitality: {hero.vitality}')
                c = input('Stat and number of points or write "cancel"\n').split()
                if c == "cancel": break
                while int(c[1]) > hero.add_points:
                    print("You don't have so many points. Please, choose again")
                    c = input('Stat and number of points or write "cancel"').split()
                if c != "cancel":
                    if c[0] == '1':
                        hero.strength += int(c[1])
                    elif c[0] == '2':
                        hero.intelligence += int(c[1])
                    elif c[0] == '3':
                        hero.sense += int(c[1])
                    elif c[0] == '4':
                        hero.vitality += int(c[1])
                    hero.add_points -= int(c[1])
                    uni = hero.up(hero)
                    hero.hp = uni.hp
                    hero.mp = uni.mp
                    hero.stam = uni.stam
            else:
                break

        execute_command(input('Choose your step: (show status, go, attack, exit)\n'))



if __name__ == '__main__':
    main()
