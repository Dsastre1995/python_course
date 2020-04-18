# def copy(existing_file, new_file):
#     with open(existing_file, 'r') as file:
#         data = file.read()

#     with open(new_file, 'w') as new_file:
#         new_file.write(data)


# copy('story.txt', 'new_story.txt')


# _________________________________________________

# def copy_and_reverse(file, new_file):
#     with open(file) as file:
#         data = file.read()

#     with open(new_file, 'w') as file2:
#         file2.write(data[::-1])

# copy_and_reverse('story.txt', 'reversed_story.txt')

# _________________________________________________

# def statistics(file_path):
#     with open(file_path) as file:
#         data = file.read()
#         statistics = {'lines': data.count('\n') + 1, 'words': len(data.split(' ')) + data.count('\n'), 'characters': len(data)}
    
#     return statistics

# print(statistics('story.txt'))

# _________________________________________________

def find_and_replace(file_path, word_to_replace, replacement_word):
    with open(file_path, 'r+') as file:
        data = file.read()
        replaced_text = data.replace(word_to_replace, replacement_word)
        file.seek(0)
        file.write(replaced_text)
        file.truncate()

find_and_reverse('story.txt', 'Alice', 'David')