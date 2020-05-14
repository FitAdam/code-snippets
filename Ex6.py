"""
user_string = str(input("Please enter a word: "))

mirror_string = user_string[::-1]
print(mirror_string)

if user_string == mirror_string:
    print("This word is a palindrome")
else:
    print("It is not a palindrome.")
"""
new_string = str(input("Hello, give me a palindrome: "))  # initial string
reversedString = []
index = len(new_string)  # calculate length of string and save in index
print("The index is ", index)
# the while loop work until the condition is met
while index > 0:
    index = index - 1  # decrement index
    print("The new decremented index is:", index)
    reversedString.append(new_string[index])  # The new list is created from the elements chosen by index position
    # when the loop is over add list is created we can print the reversed string
print("The reversed string is", reversedString)  # reversed string

mirror_string = "".join(reversedString)  # joins all list elements and put them into the string :)
print(mirror_string)

if new_string == mirror_string:
    print("This word is a palindrome")
else:
    print("It is not a palindrome.")
