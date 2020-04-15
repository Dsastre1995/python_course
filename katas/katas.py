def dig_pow(n, p):
    splited_nums = list((int(num) for num in str(n)))
    powered_nums = list(num for num in range(p, p + len(splited_nums) + 1))
    result = sum(num ** powered_num for num, powered_num in zip(splited_nums, powered_nums))
    num_result = list(filter(lambda num: n * num == result, range(1, 1000001)))

    return num_result[0] if len(num_result) > 0 else -1

print(dig_pow(695, 2))

# TODO Try by using pow()

# ________________________________________________________