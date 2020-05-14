def get_text():
    # return str(input("Type a text here:"))
    return "I love my Klaudynka"


def backwards(new_string):
    b_str = new_string.split()
    b_str.reverse()
    b_str = " ".join(b_str)
    return b_str


print(backwards(get_text()))

