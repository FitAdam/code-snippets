a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for i in a:
    if i > 5:
        b += [i]
print(b)
print(a)

user_input = int(input("Please add a number for a comparison: "))

for i in a:
    if i > user_input:
        c += [i]
print(c)




"""
fruits = ["banana", "orange", "pinapple", "banana"]

print([object for object in fruits if object == "banana"])

This would return "banana" 2 times, since there is a total of two objects called "banana" in the list "fruits".
"""

