from team import Team
from player import Player
from random import shuffle

class Tournament(Team, Player):
    def __init__(self, date, location, duration, num_participants):
        self.date = date
        self.location = location
        self.duration = duration
        self.num_participants = num_participants
        self.teams = []
        self.winner = None
        self.ranking = None

    def _ask_participant_data(self):
        players = list()
        for participant in range(self.num_participants):
            player_name = input('INTRODUCE PLAYER NAME: \n')
            player_level = input('INTRODUCE PLAYER LEVEL (0-10): \n')
            player_hand = input('INTRODUCE PLAYER PLAYING HAND (right/left): \n')
            player = Player(player_name, int(player_level), player_hand)
            players.append(player)

        return players

    def _suffle_players(self, players, level):
        for player_level in range(round(level) + 1):
            players_same_level = shuffle(list(filter(lambda player: player.level == player_level, players)))
            print(players_same_level)
            if players_same_level and len(players_same_level) > 1:
                players.extend(players_same_level)
        
        return set(players)


    def _suffle_player_with_same_level(self, players, level_average):
        players_down_average = list(filter(lambda player: player.level <= level_average, players))
        players_up_average = list(filter(lambda player: player.level > level_average, players))

        players_down_average = list(self._suffle_players(players_down_average, level_average))
        players_up_average = list(self._suffle_players(players_up_average, 9))

        # print(players_down_average)
        # print(players_up_average)
            

    def make_teams(self):
        players = self._ask_participant_data()
        players.sort(key = lambda player: player.level)

        level_average = sum([
            players[int((len(players) / 2) - 1)].level,
            players[int(len(players) / 2)].level
        ]) / 2

        print(level_average)

        self._suffle_player_with_same_level(players, level_average)

t = Tournament('08/06/2020', 'Pins Padel', 5, 4)
t.make_teams()
    # Pending TODOs:
    # - Implement logic for creating couples
    # - Add function for shuffle player with same LEVEL
    # - Add function for simmulating matches with factor lucky
    # - Add documentation
    # - Add testing