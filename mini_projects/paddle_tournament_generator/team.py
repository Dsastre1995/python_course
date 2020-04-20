from player import Player
import random

class Team(Player):
    def __init__(self, name, player1, player2, status):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.status = true
        self.afinity_factor = 2 if player1.hand != player2.hand else 1
        self.lucky_factor = random.randint(1, 10)

    def __repr__(self):
        return f'{ self.name }, formed by { self.player1.name } and { self.player2.name }'

    def quit(self):
        self.status = False