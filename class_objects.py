from desc_classes import *
#from Action import *

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
    attack_radius = None
    hp = None
    mp = None
    stam = None
    attack = None
    strength = None
    agility = None
    intelligence = None
    sense = None
    vitality = None
    effect_fis = 0
    effect_mag = 0
    step = None
    lvl = None
    x = None
    y = None

    def __init__(self, choice):
        '''

        :param choice: class name
        '''
        # TODO selecting unit's class
        self.unit = choices[choice]
        self.up = self.unit.up

    def set_start_data(self):
        self.hp = self.unit.hp_start
        self.mp = self.unit.mp_start
        self.stam = self.unit.stam_start
        self.strength = self.unit.strength_start
        self.agility = self.unit.agility_start
        self.intelligence = self.unit.intelligence_start
        self.sense = self.unit.sense_start
        self.vitality = self.unit.vitality_start
        self.step = self.unit.step_start
        self.attack_radius = self.unit.attack_radius
        self.lvl = 0


class Hero(Class):
    '''
        Hero's characterizations with their refreshing
    '''
    add_points = 5

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

    def up(self):
        pass

    def attack(self, unit, damage):
        unit.take_damage(damage)
        return unit


class Enemy(Class):
    '''
        Enemy's characterizations with their refreshing
    '''

    def take_damage(self, damage):
        '''

        :param damage: damage taken from hero

        '''
        self.hp -= damage
        if self.hp <= 0:
            print("DIIIIE, sorry =)")
            exit(0)

    def attack_hero(self, hero, damage):
        hero.take_damage(damage)
        return hero