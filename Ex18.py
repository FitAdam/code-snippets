import random


def welcome_user():
    print("Welcome to the Cows and Bulls Game!")


def generate_secret_number():
    num = (random.randrange(1000, 10000))
    num_list = []
    for x in str(num):
        num_list.append(x)

    num = num_list
    return num


def get_guessed_number():
    guess_number = list(input("Enter a number: "))
    guess_num = []
    for x in guess_number:
        guess_num.append(x)

    return guess_num


def enter_number(num):
    cows = 0
    bulls = 0
    counter = 1
    new_list = []
    condition = True
    guess_num = get_guessed_number()
    while condition:
        """For every digit that the user guessed correctly
         in the correct place, they have a “cow”"""
        if num[0] == guess_num[0]:
            cows += 1
            new_list.append(guess_num[0])

        if num[1] == guess_num[1]:
            cows += 1
            new_list.append(guess_num[1])
        if num[2] == guess_num[2]:
            cows += 1
            new_list.append(guess_num[2])
        if num[3] == guess_num[3]:
            cows += 1
            new_list.append(guess_num[3])

        """For every digit the user guessed correctly 
        in the wrong place is a “bull.”"""
        bulls_check = []
        for x in new_list:
            bulls_check.append(x)  # This will split the list
        for x in num:
            if x in guess_num: # this checks if digit is somewhere in the list
                if x not in bulls_check:  # This work against duplicates
                    bulls_check.append(x)
                    bulls += 1

        if num == guess_num:
            print("nice, you guessed after", counter, " times")

            break
        else:
            counter += 1
            print(cows, "cows,", bulls, "bulls.")
            bulls = 0
            cows = 0
            print("This is your", counter, "try.")
            guess_num = get_guessed_number()


if __name__ == "__main__":
    welcome_user()
    enter_number(generate_secret_number())
