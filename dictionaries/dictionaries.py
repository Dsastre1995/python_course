# user_info = {
#     "name": 'David Sastre',
#     "age": 25,
#     "email": 'david.sastre@email.com'
# }

# user_info_2 = dict(name = 'David', age = 25, email = 'david.sastre@email.com')

# print(user_info)
# print(user_info_2)

# ___________________________________________________

# artist = {
#     "first": 'Neil',
#     "last": 'Young',
# }

# full_name = f"{ artist['first'] } { artist['last'] }"
# print(full_name)

# ___________________________________________________

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# total_donation = 0

# for donarion in donations.values():
#     total_donation += donarion

# print(total_donation)

# for (k, v) in donations.items():
#     print(v)

# ___________________________________________________

# from random import choice
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# print(food)

# if bakery_stock.get(food):
#     print(f"{ bakery_stock.get(food) } left")
# else:
#     print("We don't make that")

# ___________________________________________________

# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 
# initial_game_state = {}.fromkeys(game_properties, 0)

# print(initial_game_state)

# ___________________________________________________

# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}

# stock_list = inventory.copy()
# stock_list.update({ 'cookie': 18 })
# stock_list.pop('cake')

# print(inventory)
# print(stock_list)

# ___________________________________________________

# alumni = { 'name': 'David', 'city': 'palma', 'coloe': 'red' }

# result = { k.upper(): v.upper() for (k, v) in alumni.items() }

# print(result)

# ___________________________________________________

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
# answer = {list1[i]: list2[i] for i in range(0, 3)}

# print(answer)

# ___________________________________________________

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# answer = { thing[0]: thing[1] for thing in person }

# ___________________________________________________

# answer = { key: 0 for key in ['a', 'e', 'i', 'o', 'u'] }

# print(answer)

# ___________________________________________________

answer = { num: chr(num) for num in range(65, 91) }

print(answer)
