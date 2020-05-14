import random

a = random.sample(range(1, 30), 5)
b = random.sample(range(1, 30), 5)
c = []
print(a)
print(b)
for i in a:
    if i in b:
        c.append(i)
print(c)

d = []
d = [x for x in a if x in b]
print(d)
