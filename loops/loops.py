# times = input('How many times do I have to tell you? \n')

# if not times:
#     print('please add a valid number')
# else:
#     print('CLEAN UP YOU ROOOOM!!!! \n' * int(times));

# __________________________________________________

# if not times:
#     print('please add a valid number')
# else:
#     for time in range(int(times)):
#         print('CLEAN UP YOU ROOOOM!!!! \n');

# __________________________________________________

# for num in range(1, 21):
#     if num == 4 or num == 13:
#         print(f'{ num } is unlucky')
#     elif num % 2 != 0:
#         print(f'{ num } is odd')
#     else:
#         print(f'{ num } is even')


# ___________________________________________________

# for x in range(1, 11):
#     print('\U0001f600' * x)
#     x += 1

# ___________________________________________________

# answer = input("Hey how's it going? \n")

# while answer != 'stop copyng me':
#     answer = input(f'{ answer } \n')

# print('UGH FINE YOU WIN')

# ___________________________________________________

# times = input('How many times do I have to tell you? \n')

# if not times:
#     print('please add a valid number')
# else:
#     for time in range(int(times)):
#         print('CLEAN UP YOU ROOOOM!!!! \n');
        
#         if time >= 4:
#             print('Are you even listening to me!!')
#             break

# ___________________________________________________

from random import randint

correct_number = 0
play_again = True
correct_number = randint(1, 10)
number = int(input('Guess a number between 1 and 10 \n'))

while play_again == True:
    if number < correct_number:
        number = int(input('Too low, please try again \n'))
    elif number > correct_number:
        number = int(input('Too hight, please try again \n'))
    else:
        print('You guessed it, good job!!')
        answer = input('Do you want to play again? (y/n) \n')
        if answer == 'y':
            play_again = True
            correct_number = randint(1, 10)
            number = int(input('Guess a number between 1 and 10 \n'))
        else:
            play_again = False
