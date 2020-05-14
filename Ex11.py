def get_int():
    return int(input("Please type a number: "))


def check_prime(num=get_int()):
    dividers = [x for x in range(1, num + 1) if num % x == 0]
    if len(dividers) == 2:
        print("It is a prime number!")
    else:
        print("This is not a Prime Number!")


check_prime()

