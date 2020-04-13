import requests
import random
import pyfiglet
import termcolor

# ___________________________________________________

# url = 'http://www.google.com'
# response = requests.get(url)

# print(response.status_code)

# ___________________________________________________

# url = 'https://www.icanhazdadjoke.com'

# response = requests.get(url, headers = { 'Accept': 'application/json' })
# response_data = response.json()

# print(response_data.get('joke'))

# ___________________________________________________

# url = 'https://www.icanhazdadjoke.com/search'

# response = requests.get(url, params = { 'term': 'cat' }, headers = { 'Accept': 'application/json' })
# response_data = response.json()

# print(response_data.get('results'))

# ___________________________________________________

url = 'https://www.icanhazdadjoke.com/search'
text = pyfiglet.figlet_format('Dsastre Jokes 3000')
title = termcolor.colored(text, 'red')

print(title)

def get_jokes(search_param):
    request = requests.get(url, params = { 'term': search_param }, headers = { 'Accept': 'application/json' })
    response = request.json().get('results')

    return response

user_search_term = input('Please tell what do you want the joke to be about: \n')
jokes = get_jokes(user_search_term)

if not jokes or len(jokes) == 0:
    print(f"I didn't find any joke about { user_search_term }, please try with an other word")
elif len(jokes) == 1:
    print('I have just found 1 joke by the term you gave as input, here it is: \n')
    print(jokes[0].get('joke'))
else:
    random_joke = random.choice(jokes)
    print(f'I have found { len(jokes) } jokes by the term you gave as input, here is one: \n')
    print(random_joke.get('joke'))