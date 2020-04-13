# print('Hello world');
# print('Good bye world');

# _____________________________________

# kms = float(input('How many KM did you run today\n'));
# print(f'Okey so you said that you have run {kms} kms, that means that you ran {round(kms * 0.621371, 2)} miles');

# _____________________________________

# number = int(input('Pargula dime un numero\n'));
# if number < 10:
#     print('Gilipollas');
# elif number > 20:
#     print('Gilipollas');
# else:
#     print('Buena esa');

# _____________________________________

# x = 57
# y = -23

# if (x >= 0) and (y >= 0):
#     print("both positive")
# elif (x < 0) and (y < 0):
#     print("both negative")
# else:
#     if (x > 0):
#         print("x is positive and y is negative")
#     else:
#         print("y is positive and x is negative")

# _____________________________________

# from random import choice, randint

# # randomly assigns values to these four variables
# actually_sick = choice([True, False])
# kinda_sick = choice([True, False])
# hate_your_job = choice([True, False])
# sick_days = randint(-10, 5)

# calling_in_sick = None

# if (actually_sick or (kinda_sick and hate_your_job)) and sick_days > 0:
#     calling_in_sick = True
# else:
#     calling_in_sick = False

# print(actually_sick)
# print(kinda_sick)
# print(hate_your_job)
# print(sick_days)
# print(calling_in_sick)

# _____________________________________

from random import choice

keep_playing = True

while keep_playing:
    print('...rock...')
    print('...paper...')
    print('...scissors...')

    player1 = input('Enter Player choice (rock / paper / scissors): \n').lower()
    player2 = choice(['rock', 'paper', 'scissors'])

    if player1 == player2:
        print('It's a tie')
    elif player1 == 'rock':
        if player2 == 'paper':
            print('Player 2 Won!')
        else:
            print('Player 1 Won!')
    elif player1 == 'paper':
        if player2 == 'rock':
            print('Player 1 Won!')
        else:
            print('Player 2 Won!')
    elif player1 == 'scissors':
        if player2 == 'paper':
            print('Player 1 Won!')
        else:
            print('Player 2 Won!')
    else:
        print('Not Valid Option')

    print(f'The value choosen by the machine was { player2 }')

    keep_playing = input('Do you want to keep playing (yes / no)? \n')

    if keep_playing == 'yes' or keep_playing == "":
        keep_playing = True
    else:
        keep_playing = False    
    