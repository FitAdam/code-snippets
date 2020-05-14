
class numbers:
    def __init__(self, path):
        # This opens a file, mode "r = read only", encoding is for ?
        self.filen = open(path, "r", encoding="utf-8")
        self.t = self.filen.read()
        
    def get_file(self):
        
        return self.t.split("\n")


class Comp(numbers):
    def __init__(self):
        self.a = prime_numbers
        self.b  = happy_numbers

    def compare(self, a , b):
        d = []
        d = [x for x in a if x in b]
        return (d)


if __name__ == "__main__":
    prime_numbers = numbers("primenumbers.txt")
    happy_numbers = numbers("happynumbers.txt")
    a = prime_numbers.get_file()
    b = happy_numbers.get_file()
    
    new_compared_numbers = Comp()
    c = new_compared_numbers.compare(a,b)
    print(c)