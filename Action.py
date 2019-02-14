name_of_classes = {
    'Warrior': 'war',
    'Magician': 'mag',
    'Prophet': 'pro',
    'Paladin': 'pal',
    'Slayer': 'slr'
}

classes = ['Warrior', 'Prophet', 'Magician', 'Slayer', 'Paladin']

# class_of_hero = 'war'
lvls = []
level = 0
while True:
    try:
        class_of_hero = name_of_classes[
            input('Please, choose your class: Warrior, Prophet, Magician, Slayer, Paladin\n')]
        break
    except KeyError:
        print('Write correct:')
        for i in classes:
            print('\t' + i)

from LVLS import *
from class_objects import *

hero = Hero(class_of_hero)
hero.set_start_data()
shown_map = None


def mains():
    pass


if __name__ == 'Action':
    mains()

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']


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
        self.maze = [['_'] * m for i in range(n)]


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
    if_show_step = False

    def __init__(self):
        pass

    def filling(self):
        # TODO filling the map and adding new enemy's objects, hero's object and exits
        self.exits = self.units['Exit']
        hero.x, hero.y = self.units['Hero'][0][1], self.units['Hero'][0][0]

        for it in self.units.keys():
            if it in choices.keys():
                for i in range(len(self.units[it])):
                    y, x = self.units[it][i][0], self.units[it][i][1]
                    self.units[it][i] = Enemy(it)
                    self.units[it][i].set_start_data()
                    self.units[it][i].y, self.units[it][i].x = y, x

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
        print('_' * self.m)

    @staticmethod
    def go(unit):
        # TODO displacement of unit to point (x, y)
        global level, lvls
        lvls[level].if_show_step = True
        draw_map()
        print('You can go to "#" field')
        xy = input('Write coordinates like "J2". If you want to cancel movement write "cancel"\n')
        if xy == "cancel":
            return unit
        while True:
            try:
                xy = [xy[0]] + [xy[1:]]
                print(xy)
                print(shown_map)
                if xy == ["c", "ancel"]:
                    return unit
                while (not xy[0] in abc) or (not xy[1].isdigit()) or not (0 <= int(xy[1]) - 1 < lvls[level].m) or not (
                        0 <= abc.index(xy[0]) < lvls[level].n) or not (
                        shown_map[abc.index(xy[0])][int(xy[1]) - 1] == '#' or shown_map[abc.index(xy[0])][int(xy[1]) - 1] == 'E'):
                    xy = input('Please, write correct data or go out with "cancel"\n')
                if xy == ["c", "ancel"]:
                    return unit
                break
            except:
                xy = input('Please, write correct data or go out with "cancel"\n')
                print(ValueError)
                continue

        if shown_map[abc.index(xy[0])][int(xy[1]) - 1] == 'E':
            level += 1
            lvls.append(lvls_names[level](Map(nms_of_levels[level][0], nms_of_levels[level][1])))
        unit.x = int(xy[1]) - 1
        unit.y = abc.index(xy[0])
        return unit

    def check_for_enemy(self):
        global hero
        for it in self.units.keys():
            if not it in ['Hero', 'Exit', 'Trap', 'Poison']:
                for xy in self.units[it]:
                    if xy.attack_radius == 1:
                        if abs(xy.x - hero.x) <= xy.attack_radius and abs(xy.y - hero.y) <= xy.attack_radius:
                            hero = xy.attack_hero(hero, xy.attack)
                    else:
                        if abs(xy.x - hero.x) <= xy.attack_radius and abs(xy.y - hero.y) <= xy.attack_radius and not (
                                abs(xy.x - hero.x) == xy.attack_radius and abs(xy.y - hero.y) == xy.attack_radius):
                            hero = xy.attack_hero(hero, xy.attack)


def draw_map():
    # TODO drawing map
    '''

    :param self: level's object
    :return: drawn map
    '''
    global shown_map
    self = lvls[level]
    dop_map = []
    for i in range(self.n):
        dop_map.append([' ']*self.m)
    for i in range(self.n):
        for j in range(self.m):
            self.maze[i][j] = '_'
    for it in self.units.keys():
        if len(self.units[it]) > 0:
            for xy in self.units[it]:
                if it in choices.keys():
                    self.maze[xy.y][xy.x] = it[0].upper()
                    dop_map[xy.y][xy.x] = xy.hp
                elif it == 'Hero':
                    self.maze[hero.y][hero.x] = 'H'
                    break
                elif it == 'Exit':
                    self.maze[xy[0]][xy[1]] = it[0]
    if self.if_show_step:
        # TODO drawing fields for movement
        if hero.step == 1:
            for i in range(self.n):
                for j in range(self.m):
                    if self.maze[i][j] != '_': continue
                    if abs(i - hero.y) <= 1 and abs(j - hero.x) <= 1:
                        self.maze[i][j] = '#'
        else:
            for i in range(self.n):
                for j in range(self.m):
                    if self.maze[i][j] != '_' or (
                            abs(i - hero.y) == hero.step and abs(j - hero.x) == hero.step): continue
                    if abs(i - hero.y) <= hero.step and abs(j - hero.x) <= hero.step:
                        self.maze[i][j] = '#'
        self.if_show_step = False

    shown_map = self.maze[:]

    print(' ', str([int(i) for i in range(1, lvls[level].m + 1)])[1:-1].split(', '))
    print('-' * (lvls[level].m * 5))
    for i in range(len(lvls[level].maze)):
        print(' ', dop_map[i])
        print(abc[i], lvls[level].maze[i])
    print('-' * (lvls[level].m * 5))


class Lvl0(Actions):
    '''
            description of lvl0
        '''

    def __init__(self, mapp):
        # TODO filling data about lvl
        self.n = mapp.n
        self.m = mapp.m
        self.maze = mapp.maze
        self.units = lvls_units[0]
        self.filling()


class Lvl1(Actions):
    '''
            description of lvl1
        '''

    def __init__(self, mapp):
        # TODO filling data about lvl
        self.n = mapp.n
        self.m = mapp.m
        self.maze = mapp.maze
        self.units = lvls_units[1]
        self.filling()


class Lvl2(Actions):
    '''
            description of lvl1
        '''

    def __init__(self, mapp):
        # TODO filling data about lvl
        self.n = mapp.n
        self.m = mapp.m
        self.maze = mapp.maze
        self.units = lvls_units[2]
        self.filling()


class Lvl3(Actions):
    '''
            description of lvl1
        '''

    def __init__(self, mapp):
        # TODO filling data about lvl
        self.n = mapp.n
        self.m = mapp.m
        self.maze = mapp.maze
        self.units = lvls_units[3]
        self.filling()


nms_of_levels = {
    0: (10, 10),
    1: (10, 10),
    2: (10, 10),
    3: (10, 10)
}
lvls_names = {
    0: Lvl0,
    1: Lvl1,
    2: Lvl2,
    3: Lvl3
}