import random
import string


def get_num():
    signs = str(input("What password do you want? "
                      "Choose between strong, medium and weak. "))
    if signs == "strong":
        return 32
    elif signs == "medium":
        return 24
    else:
        return 12


def generate_password(signs):
    password = []
    i = 0
    b = []
    # add i as long as i is less than number of signs

    while i < signs:
        i = i + 1
        password.append(random.randrange(0, 1001))
    for n, x in enumerate(password):
        if x > (random.randrange(0, 500)):
            password[n] = (random.choice(string.ascii_letters + string.punctuation))
    password.reverse()
    password = ''.join(map(str, password))
    return print("This is your password:", password)


generate_password(get_num())
