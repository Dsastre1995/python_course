import os


def check_digit_value(input_val):
    try:
        result = int(input_val)
    except ValueError:
        print('PLEASE INTRODUCE A NUMBER, OTHERWISE THIS WONT WORK')
        os._exit(1)

    return result


def get_players():
    players_collection = list()
    for num in range(int(players_number) * 2):
        player_name = input('PLAYER NAME: \n')
        player_level = check_digit_value(input('PLAYER LEVEL (1-10): \n'))
        players_collection.append(
            {'name': player_name, 'level': int(player_level)})

    return sorted(players_collection, key=lambda player: player['level'])


def createCouples(down_average_players, up_average_players):
    couples = list()
    sorted_up_average_players = sorted(
        players_up_average, key=lambda item: item['level'], reverse=True)
    for index in range(len(down_average_players)):
        couples.append(
            [down_average_players[index], sorted_up_average_players[index]])

    return couples


def calculate_player_lists(players):
    player_lists = list()
    players_down_average = list(
        filter(lambda player: player['level'] <= level_average, players))
    players_up_average = list(
        filter(lambda player: player['level'] > level_average, players))

    if not players_up_average:
        for player in players:
            players_down_average = list(filter(lambda player: players.index(
                player) < len(players) / 2, players))
            players_up_average = list(filter(lambda player: players.index(
                player) >= len(players) / 2, players))

    player_lists.append(players_down_average)
    player_lists.append(players_up_average)

    return player_lists


print('WELCOME TO THE PADDLE TORNAMENT GENERATOR PROJECT')
players_number = check_digit_value(
    input('HOW MANY COUPLES WILL BE PLAYING THIS TIME?: \n'))

check_digit_value(players_number)

players = get_players()
level_average = sum([
    players[int((len(players) / 2) - 1)]['level'],
    players[int(len(players) / 2)]['level']
]) / 2

players_lists = calculate_player_lists(players)
players_down_average = players_lists[0]
players_up_average = players_lists[1]

couples = createCouples(players_down_average, players_up_average.reverse())

print('\n FINISHED, THE COUPLES WILL BE: \n')

print('#' * 10)
print('\n')
for couple in couples:
    print(f'{couple[0]["name"]} - {couple[1]["name"]} \n')
print('#' * 10)
