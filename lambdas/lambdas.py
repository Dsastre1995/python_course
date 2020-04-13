# cube = lambda num: num ** 3

# print(cube(2))

# ___________________________________________________

# def decrement_list(collection):
#     return list(map(lambda num: num - 1, collection))

# print(decrement_list([1, 2, 3]))
# print(decrement_list([20, 14, 11]))

# ___________________________________________________

# def remove_negatives(collection):
#     return list(filter(lambda num: num >= 0, collection))

# print(remove_negatives([-1, 3, 4, -99]))
# print(remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
# print(remove_negatives([50, 60, 70]))

# ___________________________________________________

# def is_all_strings(collection):
#     return all(isinstance(item, str) for item in collection)

# print(is_all_strings(['5', 'a', 'b']))
# print(is_all_strings([5, 'a', 'b']))
# print(is_all_strings(['hello', 'goodby', 'motherfucker']))

# ___________________________________________________

# def extremes(collection):
#     return (min(collection), max(collection))

# print(extremes([1, 2, 3, 4, 5]))
# print(extremes([99, 25, 30, -7]))
# print(extremes('alcatraz'))

# ___________________________________________________

# def max_magnitude(collection):
#     return max(abs(num) for num in collection)

# print(max_magnitude([300, 20, -9001]))
# print(max_magnitude([10, 11, 12]))
# print(max_magnitude([-5, -1, -89]))

# ___________________________________________________

# def sum_even_values(*nums):
#     return sum(num for num in nums if num % 2 == 0)

# print(sum_even_values(1,2,3,4,5,6))
# print(sum_even_values(4,2,1,10))
# print(sum_even_values(1))

# ___________________________________________________

# def sum_floats(*floats):
#     return sum(fnum for fnum in floats if isinstance(fnum, float))

# print(sum_floats(1.5, 2.4, 'awesome', [], 1))
# print(sum_floats(1,2,3,4,5))

# ___________________________________________________

# def interleave(string_1, string_2):
#     return ''.join(''.join(item) for item in list(zip(string_1, string_2)))

# print(interleave('hi', 'no'))

# ___________________________________________________

# def triple_and_filter(collection):
#     filtered_collection = filter(lambda item: item % 4 == 0, collection)
#     return [num * 3 for num in filtered_collection]

# print(triple_and_filter([1,2,3,4]))
# print(triple_and_filter([6,8,10,12]))

# ___________________________________________________

def extract_full_name(collection):
    return list(map(lambda item: item['first'] + ' ' + item['last'], collection))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))