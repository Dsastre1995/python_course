def eat_junk(food):
    assert food.lower() in [
        'pizza',
        'burger',
        'kebab',
        'Noodles'
    ], 'The provided food should be junk, I dont eat health food'

    return f'NOM NOM NOM NOM, I am eating { food }'

food = input('Enter a food please: \n')
print(eat_junk(food))