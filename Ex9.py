import random
RUN = True
while RUN:
    num = random.randint(1, 10)
    i = 0
    user_number = int(input("Please guess the number from 1 to 10: "))
    # while loop works as long user number is not equal to num
    while user_number != num:
        i = i + 1
        if user_number < num:
            print("Too low!")
        elif user_number > num:
            print("Too high!")
        print("You didn't guess the number. It's your", i, "try.")
        user_number = int(input("Please guess the number from 1 to 10: "))
    if user_number == num and i == 0:
        print("Nice, you guessed the number after first time!")
        x = input("if you want to exit type exit if not press enter: ")
        if x == "exit":
            break
        else:
            continue
    if user_number == num:
        i = i + 1
        print("Nice, you guessed the number after", i, "times")
        x = input("if you want to exit type exit if not press enter: ")
        if x == "exit":
            break
        else:
            continue

