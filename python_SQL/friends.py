import sqlite3

# CREATE CONNECTION
conn = sqlite3.connect('my_friends.db')

# CREATE CURSOR
cursor = conn.cursor()

# EXECUTE QUERYS FROM CURSOR
# cursor.execute('CREATE TABLE friends ( first_name TEXT, last_name TEXT, closeness INTEGER);')

# __________________________________________

# cursor.execute("INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7);")

# __________________________________________

# WRONG WAY
# form_first = 'Dana'
# query = f"INSERT INTO friends (first_name) VALUES ('{ form_first }')"
# cursor.execute(query)

# BETTER WAY
# data = ('Steve', 'Irwin', 9)
# query = f"INSERT INTO friends VALUES (?, ?, ?);"
# cursor.execute(query, data)

# __________________________________________

# people = [
# 	("Roald","Amundsen", 5),
# 	("Rosa", "Parks", 8),
# 	("Henry", "Hudson", 7),
# 	("Neil","Armstrong", 7),
# 	("Daniel", "Boone", 3)]

# cursor.executemany('INSERT INTO friends VALUES (?, ?, ?);', people)

# for person in people:
#     cursor.execute('INSERT INTO friends VALUES (?, ?, ?);', person)
#     print(f'Inserting { person[0] }...')

# __________________________________________

# cursor.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

# for row in cursor:
#     print(row)

# print(cursor.fetchall())

# print(cursor.fetchone())

# __________________________________________



# COMMIT CHANGES
conn.commit()

# CLOSE CONNECTION
conn.close()
