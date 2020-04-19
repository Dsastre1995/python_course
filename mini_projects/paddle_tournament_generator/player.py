class Player():
    hands = ['right', 'left']

    def __init__(self, name, average_level, hand):
        if average_level > 10 or average_level < 0:
            raise ValueError('Player has to have at least a level of 0 and maximum of 10')
        if hand.lower() not in Player.hands:
            raise ValueError('Player should play with a valid hand site')
        self.name = name
        self.average_level = average_level
        self.hand = hand

    def __repr__(self):
        return f'Player { self.name } with a level of { self.average_level } plays with the { self.hand } hand'

    
player = Player('David Sastre', 6, 'right')

print(player)