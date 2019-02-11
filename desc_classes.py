import math


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
    stam_start = 62
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8
    attack_radius = 1
    step_start = 1
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
        uni.hp = player.hp + player.strength * 3 + player.vitality * 2 + player.agility - player.intelligence
        uni.mp = math.floor(player.intelligence * 1.5) + player.sense
        uni.stam = player.vitality * 2.5 + player.intelligence - player.agility + player.strength * 1.5
        return uni


class Palladin(object):
    '''
        description of unit's class
    '''
    hp_start = 150
    mp_start = 30
    stam_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8
    attack_radius = 1
    step_start = 1

    @staticmethod
    def up(player):
        '''

        :param player: unit's object (class) (hero/enemy)
        :return: unit's object

        '''
        uni = Unit()
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
    stam_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8
    attack_radius = 2
    step_start = 3

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
    stam_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8
    attack_radius = 1
    step_start = 2

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
    stam_start = 30
    strength_start = 10
    agility_start = 7
    intelligence_start = 4
    sense_start = 6
    vitality_start = 8
    attack_radius = 3
    step_start = 1

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
