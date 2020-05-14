num = int(input("Please enter the number: "))
a = []

"""
def printDivisors(num):
    i = 1
    a = []
    b = []
    # the while loop run until the condition is met
    while i <= num:
        if num % i == 0:
            print(i),
            a.append(i)

        else:
            print(i, "is not in divisors"),
            b.append(i)
        i += 1
        if i == num:
            print(a)
            print(b)



printDivisors(num)

"""
# creates a list from range 1 to num + 1(cause last number is not count in range)
listRange = list(range(1,num+1))

divisorList = []
# for every element in list
# do this
for number in listRange:
    #if num % number == 0:
    divisorList.append(number/33)

print(divisorList)