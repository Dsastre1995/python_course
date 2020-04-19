from player import Player

class Tournament(Player):
    def __init__(self, playing_date, location, start_time, end_time, couples_number):
        self.playing_date = playing_date
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.couples = None
        self.couples_number = couples_number
        self.participants = []

    def _ask_participant_data(self):
        player_name = input('INTRODUCE PLAYER NAME: \n')
        player_level = input('INTRODUCE PLAYER LEVEL (0-10): \n')
        player_hand = input('INTRODUCE PLAYER PLAYING HAND (right/left): \n')

        return Player(player_name, int(player_level), player_hand)

    def add_pariticipants(self):
        count = 1
        for couples in range(self.couples_number):
            print(f'\n\nCREATING PARTICIPANT { count }... \n\n')
            player1 = self._ask_participant_data()
            count += 1
            # ______________________________________________

            print(f'\n\nCREATING PARTICIPANT { count }... \n\n')
            player2 = self._ask_participant_data()
            count += 1

            self.participants.extend([player1, player2])

t = Tournament('14/5/2020', 'Pins Padel', '09:00', '13:00', 2)
t.add_pariticipants()

for player in t.participants:
    print(player)



    # Pending TODOs:
    # - Implement logic for creating couples
    # - Add function for shuffle player with same LEVEL
    # - Add function for simmulating matches with factor lucky
    # - Add documentation
    # - Add testing