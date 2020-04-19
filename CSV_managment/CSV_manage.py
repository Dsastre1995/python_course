from csv import writer, reader

# def add_user(first_name, last_name):
#     with open('users.csv', 'a') as file:
#         csv_writer = writer(file)
#         csv_writer.writerow([first_name, last_name])


# add_user('David', 'Sastre')


# ___________________________________________________

# def print_users():
#     with open('users.csv') as file:
#         csv_reader = reader(file)
#         next(csv_reader)
#         for row in csv_reader:
#             print(row[0] + ' ' + row[1])

# print_users()

# ___________________________________________________

# def find_user(first_name, last_name):
#     with open('users.csv') as file:
#         csv_reader = reader(file)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return f'{ first_name } { last_name } not found.'

# print(find_user('Pepe', 'Turing'))

# ___________________________________________________

# def update_user(old_first_name, old_last_name, new_first_name, new_last_name):
#     with open('users.csv') as file:
#         csv_rider = reader(file)
#         rows = list(csv_rider)
    
#     count = 0
#     with open('users.csv', 'w') as file:
#         csv_rider = writer(file)
#         for row in rows:
#             if row[0] == old_first_name and row[1] == old_last_name:
#                 csv_rider.writerow([new_first_name, new_last_name])
#                 count += 1
#             else:
#                 csv_rider.writerow(row)

#     return f'Users updated: { count }'

# print(update_user('Alan', 'Turing', 'David', 'Sastre'))

# ___________________________________________________

def delete_users(first_name, last_name):
    not_matched_rows = []
    count = 0
    with open('users.csv') as file:
        csv_reader = reader(file)
        for row in list(csv_reader):
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                not_matched_rows.append(row)

    with open('users.csv', 'w') as file:
        csv_writer = writer(file)
        for row in not_matched_rows:
            csv_writer.writerow(row)

    return f'Users deleted: { count }'

print(delete_users('Alan','Turing'))
