# class Vehicle:
#     pass

# car = Vehicle()
# boat = Vehicle()

# print(car)
# print(boat)

# ___________________________________________________

# class Comment:
#     def __init__(self, username, text, likes = 0):
#         self.username = username
#         self.text = text
#         self.likes = likes

# c = Comment('David', 'This is my first comment, I hope you like it!', 45)
# another_comment = Comment('Luis', 'This is my last comment. I will leave this social media, fuck you all!!')

# print(c.username)
# print(c.text)
# print(c.likes)

# print(another_comment.username)
# print(another_comment.text)
# print(another_comment.likes)

# ___________________________________________________

# class BankAccount:
#     def __init__(self, owner, balance = 0.0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, money_amount):
#         self.balance += money_amount
#         return self.balance

#     def withdraw(self, money_amount):
#         self.balance -= money_amount
#         return self.balance

# david_acct = BankAccount('David', 10000)
# luis_acct = BankAccount('Luis', 14000)

# print(david_acct.balance)
# print(luis_acct.balance)

# print(david_acct.deposit(4000))
# print(luis_acct.withdraw(4000))

# print({f'The balance of { david_acct.owner } now is: { david_acct.balance }'})
# print({f'The balance of { luis_acct.owner } now is: { luis_acct.balance }'})

# ___________________________________________________

# class Chicken:
#     total_eggs = 0

#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#         self.eggs = 0

#     def lay_egg(self):
#         self.eggs += 1
#         Chicken.total_eggs += 1

#         return self.eggs

# c1 = Chicken('David', 'Partridge Silkie')
# c2 = Chicken('Luis', 'Speckled Sussex')

# print(Chicken.total_eggs)
# c1.lay_egg()
# print(Chicken.total_eggs)
# c2.lay_egg()
# c2.lay_egg()
# print(Chicken.total_eggs)

# ___________________________________________________

# class Character:
#     def __init__(self, name, hp, level):
#         self.name = name
#         self.hp = hp
#         self.level = level

# class NPC(Character):
#     def __init__(self, name, hp, level, speak_text):
#         super().__init__(name, hp, level)
#         self.speak_text = speak_text

#     def speak(self):
#         return f'{ self.name } says: { self.speak_text }'


# villager = NPC('Misco', 100, 15, 'Hey dude, I am looking for my friend. Is called Lickma, Lickma balls!')

# print(villager.name)
# print(villager.hp)
# print(villager.level)
# print(villager.speak())

# ___________________________________________________

# class Mother:
#     def __init__(self):
#         self.eye_color = 'brown'
#         self.hair_color = 'dark brown'
#         self.hair_type = 'curly'

# class Father:
#     def __init__(self):
#         self.eye_color = 'blue'
#         self.hair_color = 'blonde'
#         self.hair_type = 'straight'

# class Child(Mother, Father):
#     def __init__(self):
#         super().__init__()


# c = Child()
# print(c.eye_color)
# print(c.hair_color)
# print(c.hair_type)

# ___________________________________________________

class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return f'{ self.num_cars } cars train'

    def __len__(self):
        return self.num_cars

train = Train(16)
print(train)
print(len(train))