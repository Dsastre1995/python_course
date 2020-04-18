# def eat_junk(food):
#     assert food.lower() in [
#         'pizza',
#         'burger',
#         'kebab',
#         'Noodles'
#     ], 'The provided food should be junk, I dont eat health food'

#     return f'NOM NOM NOM NOM, I am eating { food }'

# food = input('Enter a food please: \n')

# print(eat_junk(food))

# ______________________________________________________

def eat(food, is_healthy):
    health_ending = 'because my body is a temple'
    unhealth_ending = 'because YOLO'

    if is_healthy:
        return f'I am eating { food }, { health_ending }'
    return f'I am eating { food }, { unhealth_ending }'

def nap(num_hours):
    long_nap = 'I wont sleep well tonight'
    short_nap = 'I am fresh and probably I will sleep well enought tonight'

    if num_hours >= 2:
        return f'I sleept { num_hours } hours, { long_nap }'
    return f'I sleept just {num_hours} hour, { short_nap }'