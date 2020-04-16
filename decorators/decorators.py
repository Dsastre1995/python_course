from functools import wraps

# import time
# def speed_test(fn):
#     @wraps(fn)
#     def wrapper(*args, **kargs):
#         start_time = time.time()
#         result = fn(*args, **kargs)
#         total_time = time.time()
#         print(f'Executing: { fn.__name__ }')
#         print(f'The operation took { total_time - start_time } seconds')
#         return result
#     return wrapper

# @speed_test
# def multi_sum_generator():
#     return sum(x for x in range(90000000))

# @speed_test
# def multi_sum_comprenhension():
#     return sum([x for x in range(90000000)])


# print(multi_sum_comprenhension())
# print(multi_sum_generator())

# _______________________________________________________

# def show_args(fn):
#     @wraps(fn)
#     def wrapper(*args, **kargs):
#         print(f'Here are the args { args }')
#         print(f'Here are the kargs { kargs }')
#         return fn(args, kargs)

#     return wrapper

# @show_args
# def do_something(*args, **kargs):
#     print('Hello world')
#     return wrapper

# @show_args
# def do_something(*args, **kargs):
#     print('Hello world')


# do_something(1, 2, 3,a="hi",b="bye")

# _______________________________________________________

# def double_return(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         result = [fn(*args, **kwargs), fn(*args, **kwargs)]
#         return result
#     return wrapper

# @double_return
# def greet(name):
#     return f"Hi, I'm { name }"


# print(greet('David'))

# _______________________________________________________

# def ensure_fewer_than_three_args(fn):
#     @wraps(fn)
#     def wrapper(*args):
#         if len(args) >= 3:
#             return 'Too many arguments'
#         return fn(*args)
    
#     return wrapper

# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)

# print(add_all(1, 56, 78, 45, 1259, 45, 46468))

# _______________________________________________________

# def only_ints(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if all(isinstance(x, int) for x in args):
#             return fn(*args)
#         return 'Please only invoke with integers.'

#     return wrapper

# @only_ints
# def add(*args):
#     return sum(args)

# print(add(15, 46, 4894, 64654, 5))

# _______________________________________________________

# def ensure_authorised(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if any(name == 'role' and value == 'admin' for (name, value) in kwargs.items()):
#             return fn(*args, **kwargs)
#         return 'Unauthorized'

#     return wrapper

# @ensure_authorised
# def show_secret(*args, **kwargs):
#     return 'shhhh, do not tell anybosy'

# print(show_secret(role='administrador'))

# _______________________________________________________
import time

def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print('Waiting {}s before running {}'.format(val, fn.__name__))
            time.sleep(val)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hay(name):
    print(f'Hi, { name }')

say_hay('David')