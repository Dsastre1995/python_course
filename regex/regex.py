import re

# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
# res = pattern.search('878797987987877983789237982375987439857349875897348957349875347689740380498')
# print(re)
# re = pattern.findall('Call me at 663 014-1000 or 666 642-4288')
# print(re)

# ____________________________________________________________

# phone_pattern = re.compile(r'\b\d{3} \d{3}-\d{4}\b')

# def find_phone_number(input):
#     match = phone_pattern.search(input)
#     return None if not match else match.group()

# print(find_phone_number('If you want to have fun, just call me at 798 457-4359'))
# print(find_phone_number('If you want to have fun, just call me at 798 457-43597889798987987'))

# def find_phone_numbers(input):
#     match = phone_pattern.findall(input)
#     return match

# print(find_phone_numbers('You can find me at any of this numbers: 465-895-1324, 644 879-1325 or 648 564-6564'))
# print(find_phone_numbers('You can find me at any of this numbers: 466564654546748564687875487898789754897894897847'))

# def is_valid_phone(input):
#     phone_validation_pattern = re.compile(r'ˆ\d{3} \d{3}-\d{4}$')
#     match = phone_pattern.search(input)
#     # match = phone_pattern.fullmatch(input)
#     return False if not match else True

# print(is_valid_phone('456 131-7987'))
# print(is_valid_phone('456 131-7987ewf646we8f87we'))
# print(is_valid_phone('456 131-7987456e4f65w4e5'))

# ____________________________________________________________

# def is_valid_time(input):
#     time_pattern = re.compile(r'^\d{2}?:\d{2}$')
#     match = time_pattern.search(input)

#     return True if match else False

# # def is_valid_time(input):
# #     pattern = re.compile(r'^\d\d?:\d\d$')
# #     match = pattern.search(input)
# #     if match:
# #         return True
# #     return False


# print(is_valid_time('12:00'))

# ____________________________________________________________

# def parse_bytes(input):
#     byte_pattern = re.compile(r'\b[0-1]{8}\b')
#     match = byte_pattern.findall(input)

#     return match

# print(parse_bytes('11010101 101 323'))
# print(parse_bytes('My data is: 10101010 11100010'))
# print(parse_bytes('lkgerljgerj'))

# ____________________________________________________________

def parse_date(input):
    date_pattern = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$')
    match = date_pattern.search(input)
    
    if match:
        return {
            'd': match.group(1),
            'm': match.group(2),
            'y': match.group(3),
        }
    else:
        return None

print(parse_date('12,04,2003'))

