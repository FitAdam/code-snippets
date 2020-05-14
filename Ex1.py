import datetime


def copy_message(message):
    copies = int(input("How many copies do you want to print out? "))
    # If you want to print (copies) x lines of something, you can use a for loop:
    for i in range(copies):
        print(message)


while True:
    message = str(input("Enter your message: "))
    if message == "break":
        break
    else:
        copy_message(message)
