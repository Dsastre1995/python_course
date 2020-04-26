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

    def _createCouples(self, players_down_average, players_up_average):
        couples = list()
        sorted_up_average_players = sorted(players_up_average, key=lambda player: player.level, reverse=True)
        for index in range(len(players_down_average)):
            couples.append([players_down_average[index], sorted_up_average_players[index]])

        return couples

    def _suffle_players(self, players):
        result = list()
        for level in range(1, 11):
            same_level_players = list(filter(lambda player: player.level > level - 1 and player.level <= level, players))
            if len(same_level_players) > 1:
                shuffle(same_level_players)
            result.extend(same_level_players)

        return result

    def _split_player_by_level(self, players):
        level_average = sum([
            players[int((len(players) / 2) - 1)].level,
            players[int(len(players) / 2)].level
        ]) / 2

        down_average_players = list(filter(lambda player: player.level <= level_average, players))
        up_average_players = list(filter(lambda player: player.level > level_average, players))

        return [down_average_players, up_average_players]
            

    def make_teams(self):
        players = self._ask_participant_data()
        players = self._suffle_players(players)
        splited_players = self._split_player_by_level(players)

        while len(splited_players[0]) > len(splited_players[1]):
            ssplited_players[0].append(splited_players[1].pop())

        couples = self._createCouples(splited_players[0], splited_players[1])

        for (index, couple) in enumerate(couples):
            team = Team(f'team-{ index + 1 }', couple[0], couple[1])
            self.teams.append(team)

    def _create_possible_rounds(self):
        shuffle(self.teams)
        round_test = [[self.teams[x], self.teams[x + 1]] for x in range(0, len(self.teams), 2)]

        return round_test

    def set_ranking(self):
        rounds_num = self.num_participants if len(self.num_participants) % 2 != 0 else len(self.num_participants) - 1
        rounds = []

        for i in range(rounds_num):
            possible_rounds = self._create_possible_rounds()
            already_exists_in_round = any(possible_rounds in round for round in rounds for possible_round in possible_rounds):
            if already_exists_in_round:

            else:
                rounds.append(possible_round)

t = Tournament('08/06/2020', 'Pins Padel', 5, )
t.make_teams()
t.set_ranking()
print(t.ranking)

    # Pending TODOs:
    # - Implement logic for creating couples
    # - Add function for shuffle player with same LEVEL
    # - Add function for simmulating matches with factor lucky
    # - Add documentation
    # - Add testing