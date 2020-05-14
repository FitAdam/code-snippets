"""def get_int():
    return int(input("Please type a number: "))


# Recursive function

def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        return fibonacci(num - 1) + fibonacci(num - 2)


def set_number(my_num=get_int()):
    for num in range(1, my_num + 1):
        print(num, ":", fibonacci(num))


set_number()"""

fibonacci_cache = {}


def fibonacci(num):
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num == 1:
        value = 1
    elif num == 2:
        value = 1
    elif num > 2:
        value = fibonacci(num - 1) + fibonacci(num - 2)
    fibonacci_cache[num] = value
    return value


def get_int():
    return int(input("Please type a number: "))


def set_number(my_num=get_int()):
    for num in range(1, my_num + 1):
        print(num, ":", fibonacci(num))


set_number()
