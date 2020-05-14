def get_list():
    a = [2 ** x for x in range(10)] + [3 ** x for x in range(10)]

    return a


def new_list(lst):
    lst = set(lst)
    a = list(lst)
    a.sort()
    return a


abc = [1, 2, 3, 4, 4, 5]


def kills_duplicates(abc):
    y = []
    for i in abc:
        if i not in y:
            y.append(i)
    return print(y)


print(get_list())

print(new_list(get_list()))

kills_duplicates(abc)
