class Player():
    hands = ['right', 'left']

    def __init__(self, name, level, hand):
        if level > 10 or level < 0:
            raise ValueError('Player has to have at least a level of 0 and maximum of 10')
        if hand.lower() not in Player.hands:
            raise ValueError('Player should play with a valid hand site')
        self.name = name
        self.level = level
        self.hand = hand

    def __repr__(self):
        return f'Player { self.name } with a level of { self.level } plays with the { self.hand } hand'