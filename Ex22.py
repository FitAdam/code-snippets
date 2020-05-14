def readfile():
    # This opens a file, mode "r = read only", encoding is for ?
    filen = open("file_ex22", "r", encoding="utf-8")
    t = filen.read()
    # This stores a text in variable t
    print("t: ", t)
    # This creates list by splitting elements betewen spaces \n
    l = t.split("\n")
    print("l: ",l)
    # This creates a set from list (set has uniqe elements, no dublicates)
    short = set(l)
    print("short: ", short)
    # This calculates the number of elements
    size = len(short)
    print("size: ", size)
    print("There are %d names in the list" % size)
    print("The names are: " + ", ".join(short))

readfile()