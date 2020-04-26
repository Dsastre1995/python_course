from player import Player
import random

class Team(Player):
    def __init__(self, name, player1, player2):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.status = True
        self.afinity_factor = 2 if player1.hand != player2.hand else 1
        self.lucky_factor = random.randint(1, 10)
        self.level_average = (((self.player1.level + self.player2.level) / 2) + self.afinity_factor + self.lucky_factor) / 3

    def __repr__(self):
        return f'{ self.name }, formed by { self.player1.name } and { self.player2.name }, has a level { self.level_average } \n'

    def quit(self):
        self.status = False