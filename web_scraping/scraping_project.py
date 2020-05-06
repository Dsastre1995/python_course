from bs4 import BeautifulSoup
import requests
from random import choice
from csv import DictReader

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def get_hints(extra_info_url, author):
    more_info_response = requests.get(extra_info_url)
    more_info_soup = BeautifulSoup(more_info_response.text, 'html.parser')
    author_first_name = author.split(' ')[0]
    author_last_name = author.split(' ')[1]
    author_born_date = more_info_soup.find(class_ = 'author-born-date').get_text()
    author_born_location = more_info_soup.find(class_ = 'author-born-location').get_text()

    author_born_data = f'Author was born on  { author_born_date } { author_born_location }' 
    author_first_name_initial = f"The author's first name starts with { author_first_name[0] }"
    author_last_name_initial = f"The author's last name starts with { author_last_name[0] }"

    return [author_born_data, author_first_name_initial, author_last_name_initial]

def read_quotes(filename):
    with open(filename, 'r') as file:
        dict_rider = DictReader(file)
        return list(dict_rider)

def play_game(quotes):
    random_quote = choice(quotes)
    guess = ''
    hints = get_hints(random_quote.get('bio-info'), random_quote.get('author'))
    remaining_guesses = 4
    keep_playing = ''

    print("\n ######################################################## \n")

    print("WELCOME TO THE QUOTE GUESSER GAME, LET'S PLAY!!! \n")
    print("Here's a quote \n")
    print(f'{ random_quote.get("text") } \n')

    while guess.lower() != random_quote.get('author').lower() and remaining_guesses > 0:
        guess = input(f'\n Who said this quote - remaining guesses: { remaining_guesses } - \n\n')
        if guess.lower() == random_quote.get('author').lower():
            print('YOU GUESSED RIGHT!!')
            break
        remaining_guesses -= 1
        if remaining_guesses == 3: 
            print('Wrong!! Here there is a hint \n')
            print(hints[0])
        elif remaining_guesses == 2:
            print('Wrong!! Here there is a hint \n')
            print(hints[1])
        elif remaining_guesses == 1:
            print('Here there is a hint \n')
            print(hints[2])
        else:
            print(f'You run out of guesses, the answer was { random_quote.get("author") }')
            break

    while keep_playing.lower() not in ('yes', 'y', 'no', 'n'):
        keep_playing = input('Would you like to play again (Y/N)')

    if keep_playing in ('yes', 'y'):
        play_game(quotes)
    else:
        print('Bye bye')

quotes = read_quotes('quotes.csv')
play_game(quotes)