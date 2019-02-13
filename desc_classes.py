import math


class Unit(object):
    hp = None
    mp = None
    stam = None


class Warrior(object):
    '''
        description of unit's class
    '''
    strength_start = 11
    agility_start = 10
    intelligence_start = 4
    sense_start = 5
    vitality_start = 10
    attack_radius = 1
    attack_start = 2 * strength_start + math.floor(0.5*agility_start) + math.floor(0.25 * vitality_start)
    step_start = 2
    hp_start = 10 * vitality_start + math.floor(0.5*strength_start)
    mp_start = 100
    stam_start = strength_start + math.ceil(0.25*vitality_start)
    coof = {
        0: [1, 3, 2, 1],
        1: [1, 1.5, 1],
        2: [1, 2.5, 1, -1, 1.5],
        3: [1, 2, 3, 1.5, -1, 1]
    }

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit()
        uni.hp = 10 * player.vitality + math.floor(0.5*player.strength)
        uni.mp = math.floor(player.intelligence * 1.5) + player.sense
        uni.stam = player.strength + math.ceil(0.25*player.vitality)
        return uni


class Palladin(object):
    '''
        description of unit's class
    '''
    strength_start = 10
    agility_start = 4
    intelligence_start = 6
    sense_start = 5
    vitality_start = 15
    attack_radius = 1
    attack_start = 2 * vitality_start + math.floor(0.3 * sense_start) + strength_start
    step_start = 1
    hp_start = 12 * vitality_start + strength_start
    mp_start = math.floor(0.75 * intelligence_start) + math.ceil(0.25*agility_start)
    stam_start = vitality_start + agility_start + math.ceil(0.55 * strength_start)

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit()
        uni.hp = 12 * player.vitality + player.strength
        uni.mp = math.floor(0.75 * player.intelligence) + math.ceil(0.25*player.agility)
        uni.stam = player.vitality + player.agility + math.ceil(0.55 * player.strength)
        return uni


class Magician(object):
    '''
        description of unit's class
    '''
    strength_start = 5
    agility_start = 9
    intelligence_start = 15
    sense_start = 11
    vitality_start = 10
    attack_radius = 3
    attack_start = 3 * intelligence_start + math.floor(0.5 * agility_start) + math.floor(0.25 * sense_start)
    step_start = 3
    hp_start = math.ceil(4 * vitality_start + 0.5 * strength_start + 2 * intelligence_start)
    mp_start = 12 * intelligence_start + math.ceil(0.25 * agility_start)
    stam_start = 0

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit
        uni.hp = math.ceil(4 * player.vitality + 0.5 * player.strength + 2 * player.intelligence)
        uni.mp = 12 * player.intelligence + math.ceil(0.25 * player.agility)
        uni.stam = 0
        return uni


class Slayer(object):
    '''
        description of unit's class
    '''
    strength_start = 9
    agility_start = 14
    intelligence_start = 4
    sense_start = 8
    vitality_start = 5
    attack_radius = 1
    attack_start = 2 * strength_start + math.floor(0.5 * agility_start) + math.floor(0.25 * vitality_start)
    step_start = 2
    hp_start = 8 * vitality_start + math.ceil(0.5 * strength_start + 0.25 * agility_start)
    mp_start = math.ceil(0.5 * intelligence_start + 1.2 * agility_start + 0.18 * sense_start)
    stam_start = agility_start + math.ceil(0.25 * vitality_start)

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit
        uni.hp = 8 * player.vitality + math.ceil(0.5 * player.strength + 0.25 * player.agility)
        uni.mp = math.ceil(0.5 * player.intelligence + 1.2 * player.agility + 0.18 * player.sense)
        uni.stam = player.agility + math.ceil(0.25 * player.vitality)
        return uni


class Prophet(object):
    '''
        description of unit's class
    '''
    strength_start = 7
    agility_start = 8
    intelligence_start = 8
    sense_start = 10
    vitality_start = 7
    attack_radius = 4
    attack_start = math.floor(1.5 * sense_start) + agility_start + math.ceil(1.2 * intelligence_start)
    step_start = 4
    hp_start = math.floor(1.8 * intelligence_start + 1.2 * agility_start + 3 * sense_start)
    mp_start = 10 * intelligence_start + 3 * agility_start + sense_start
    stam_start = 0

    @staticmethod
    def up(player):
        '''

            :param player: unit's object (class) (hero/enemy)
            :return: unit's object
        '''
        uni = Unit
        uni.hp = math.floor(1.5 * player.intelligence + 1.5 * player.agility + 0.8 * player.sense)
        uni.mp = math.floor(10 * player.intelligence + 3 * player.agility + player.sense)
        uni.stam = 0
        return uni
