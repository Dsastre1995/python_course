# def week():
#     week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     for day in week:
#             yield day

# days = week()
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))

# ___________________________________________________

# def yes_or_no():
#     count = 1
#     while True:
#         yield 'yes' if count % 2 != 0 else 'no'
#         count += 1

# gen = yes_or_no()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# ___________________________________________________

# def make_song(count = 99, beverage = 'soda'):
#     for num in range(count, -1, -1):
#         if num > 1:
#             yield f'{ num } bottles of { beverage } on the wall'
#         elif num == 1:
#             yield f'Only { num } bottle of { beverage } left'
#         else:
#             yield f'No more { beverage }'

# deafult_song = make_song(5)
# print(next(deafult_song))
# print(next(deafult_song))
# print(next(deafult_song))
# print(next(deafult_song))
# print(next(deafult_song))
# print(next(deafult_song))

# ___________________________________________________

# def get_multiples(num = 1, count = 10):
#     for range_num in range (1, count + 1):
#         yield num * range_num

# default_multiples = get_multiples(2, 20)
# print(list(default_multiples))

# ___________________________________________________

# def get_unlimited_multiples(number = 1):
#     count = 1
#     while True:
#         yield number * count
#         count += 1

# unlimited = get_unlimited_multiples(2)
# print([next(unlimited) for i in range(15)])

# ___________________________________________________