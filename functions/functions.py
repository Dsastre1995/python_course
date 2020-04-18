# def make_noise():
#     """
#     Print some random text
#     >>> make_noise()
#     THE CROWD GOES WILD
#     """
#     print('THE CROWD GOES WILD')

# make_noise()

# ___________________________________________________

# from random import random

# def coin_flip():
#     if random() <= 0.5:
#         return 'Heads'
#     else:
#         return 'Tails'

# print(coin_flip())

# ___________________________________________________

# def speak_pig():
#     return 'oink'

# print(speak_pig())

# ___________________________________________________

# def generate_evens():
#     return [num for num in range(1,50) if num % 2 == 0]

# print(generate_evens())

# ___________________________________________________

# def yell(string):
#     """
#     Converts parameter into upper
#     >>> yell('hola me llamo david')
#     'HOLA ME LLAMO DAVID!'

#     >>> yell(' ')
#     ' !'
#     """
#     return f"{ string.upper() }!"

# print(yell("Let's play magic the gathering"))

# ___________________________________________________

# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == '$':
#             count += 1
#     return count

# print(count_dollar_signs('$uper $size'))

# ___________________________________________________

def speak(animal_name = 'dog'):
    """
    Get the animal sound by the animal name, default param is dog
    >>> speak('dog')
    'woof'

    >>> speak(' ')
    '?'

    >>> speak('elephant')
    '?'
    """

    animals = [
        {'name': 'pig', 'sound': 'oink'},
        {'name': 'duck', 'sound': 'quack'},
        {'name': 'cat', 'sound': 'meow'},
        {'name': 'dog', 'sound': 'woof'},
    ]

    selected_animal = [animal for animal in animals if animal['name'] == animal_name]

    if len(selected_animal) == 0:
        return '?'

    return selected_animal[0]['sound']
    


print(speak('cat'))
                
# ___________________________________________________

# def product(val1, val2):
#     return val1 * val2;

# print(product(2, -2))

# ___________________________________________________

# def return_day(num_day):
#     days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}

#     if num_day < 1 or num_day > 7:
#         return None
    
#     return days.get(num_day)

# print(return_day(45))

# ___________________________________________________

# def last_element(num_list = []):
#     if len(num_list) == 0:
#         return None

#     return num_list.pop()

# print(last_element())

# ___________________________________________________

# def number_compare(val1, val2):
#     if val1 > val2:
#         return 'First is greater'
#     elif val1 < val2:
#         return 'Second is greater'

#     return 'Numbers are equal'



# print(number_compare(4, 1))
# print(number_compare(4, 6))
# print(number_compare(4, 4))

# ___________________________________________________

# def single_letter_count(string, letter):
#     return string.lower().count(letter.lower())

# print(single_letter_count('Hello, my name is David Sastre San Emeterio', 's'))

# ___________________________________________________

# def multiple_letter_count(word):
#     return { char: word.count(char) for char in word }

# print(multiple_letter_count('tusmuertos'))

# ___________________________________________________

# def list_manipulation(items_list, command, location, value):
#     if command == 'remove' and location == 'beginning':
#         items_list.pop(0)
#     elif command == 'remove' and location == 'end':
#         items_list.pop()
#     elif command == 'add' and location == 'beginning':
#         items_list.insert(0, value)
#     elif command == 'add' and location == 'end':
#         items_list.append(value)
#     else:
#         return items_list

#     return items_list

#     print(list_manipulation([1, 2, 3, 4], 'remove', 'beginning', 89))

# ___________________________________________________

# def is_palindrome(string):
#     no_whitespaces = string.replace(' ', '')
#     return no_whitespaces == no_whitespaces[::-1]

# print(is_palindrome('a man a plan a canal panama'))

# ___________________________________________________

# def frequency(items_list, search_param):
#     return items_list.count(search_param)

# print(frequency([1, 2, 3, 4, 4, 4], 4))
# print(frequency([True, False, True, True], True))

# ___________________________________________________

# def multiply_even_numbers(collection):
#     even_collenction = [item for item in collection if item % 2 == 0]
#     result = 1
#     for num in even_collenction:
#         result *= num
#     return result

# print(multiply_even_numbers([2, 3, 4, 5, 6, 8]))

# ___________________________________________________

# def capitalize(string):
#     return string[0].upper() + string[1::]

# print(capitalize('david'))

# ___________________________________________________

# def compact(collection):
#     return [item for item in collection if item]

# print(compact([0, 1, 2, "", False, None, 'All done']))

# ___________________________________________________

# def intersection(collection_1, collection_2):
#     set_1 = set(collection_1)
#     set_2 = set(collection_2)

#     return list(set_1.intersection(set_2))

# print(intersection([1, 2, 3], [2, 3, 4]))
# print(intersection(['a', 'b', 'z'], ['x', 'y', 'z', 'w']))

# ___________________________________________________

# def is_even(num):
#     return num % 2 == 0

# def partition(collection, callback_def):
#     truthy_list = [num for num in collection if callback_def(num)]
#     falsy_list = [num for num in collection if not callback_def(num)]

#     return [truthy_list, falsy_list]

# print(partition([1, 2, 3, 4], is_even))

# ___________________________________________________

# def contains_purple(*args):
#     return len([item for item in list(args) if item == 'purple']) > 0
#     return 'purple' in list(args)

# print(contains_purple('purple', 25))

# ___________________________________________________

# def combine_words(word, **args):
#     if 'prefix' in args:
#         return args['prefix'] + word
#     elif 'suffix' in args:
#         return word + args['suffix']
#     else:
#         return word

# print(combine_words('gun', prefix='machine'))
# print(combine_words('home', suffix='office'))
# print(combine_words('home'))

# ___________________________________________________

# def count_sevens(*args):
#     return args.count(7)

# nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

# result1 = count_sevens(1, 4, 7)
# result2 = count_sevens(*nums)

# print(result1)
# print(result2)

# ___________________________________________________

# def reverse_text(text):
#     text_pieces = text.split()
#     result = '';

#     for item in reversed(text_pieces):
#         result += item + ' '

#     return result

# print(reverse_text(input('Put a sentence: \n')))

