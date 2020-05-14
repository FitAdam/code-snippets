import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [random.randint(1, 10) for q in range(5)]
print(c)
d = [random.randint(1, 10) for q in range(5)]
print(d)
listAB = []
listCD = []
"""
for x in b:
    if x in a:
        c.append(x)
print(c)
"""
[listAB.append(x) for x in b if x in a]
print(listAB)
[listCD.append(x) for x in c if x in d]
print(listCD)
