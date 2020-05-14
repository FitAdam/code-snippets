


def Supply():
    age = int(input("Please enter your age: "))
    ammount_per_day = int(input("Please type how many candies you eat per day: "))
    supply_needed = (100 - age) * (ammount_per_day * 365)

    return print(f"You need {supply_needed} candies to have it enough until you will have 100 years. ")



Supply()