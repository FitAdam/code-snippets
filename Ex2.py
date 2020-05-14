num = int(input("Please entere a number: "))


# od = 1,3,5
# even = 2,4,6
def check_num(num):
    if num % 2 == 0:
        print(num, " is even.")
    else:
        print(num, "is odd.")
    if num % 4 == 0:
        print("The number is multiple of four.")


check_num(num)

check = int(input("the number will be divided by: "))

if num % check == 0:
    print(num, "the number can be divided by ", check)
else:
    print(num, "cannot be divided by", check)

print(num/check)