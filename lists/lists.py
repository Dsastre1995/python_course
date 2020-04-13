# list1 = ['Banana', 'Apples', 'meat', 'Cheese', 'Carrots', 'Melon', 'WC paper', 45, True, 98.46878794, False]
# list2 = list(range(1, 10))
# print(list1)
# print(list2)
# print(len(list1))
# print(len(list2))

# ___________________________________________________

# my_stuff = ['This', 'is', 'my', 'first', 'list', 'in', 'python', 45.5689]
# nums = list(range(1, 100))

# print(my_stuff)
# print(nums)

# ___________________________________________________

# people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]

# people[0] += 'h' 
# people[4] = 'Jeffrey'
# people[5] = 'Aparna'

# print(people)

# ___________________________________________________

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# result = ''

# for sound in sounds:
#     result += sound.upper()

# print(result)

# ___________________________________________________

# instructors = []
# instructors.append('Blue')
# instructors.insert(0, 'Colt')
# instructors.extend(['Lisa'])

# print(instructors)

# ___________________________________________________

# instructors = []

# instructors.extend(['Colt', 'Blue', 'Lisa'])
# instructors.pop()
# instructors.pop(0)
# instructors.insert(0, 'Done')

# print(instructors)

# ___________________________________________________

# Bonus - LIST COMPREHENSION

# answer = [name[0] for name in ['Elie', 'Tim', 'Matt']]
# answer2 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]

# print(answer)
# print(answer2)

# ___________________________________________________

# answer = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]]
# answer2 = [name[::-1].lower() for name in ['Elie', 'Tim', 'Matt']]

# print(answer)
# print(answer2)

# ___________________________________________________

# answer = [num for num in range(1, 101) if num % 12 == 0]

# print(answer)

# ___________________________________________________

# answer = [leter for leter in 'amazing' if leter not in 'aeiou']

# print(answer)

# ___________________________________________________

# answer = [[num for num in range(0, 3)] for num in range(0, 3)]

# print(answer)

# ___________________________________________________

answer = [[i for i in range(10)] for num in range(10)]

print(answer)

