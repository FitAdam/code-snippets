"""

def binary_search():
    while True:
        a = [1, 3, 5, 30, 42, 43, 500]
        print("\n", a, "\n That's the list that we are going to check.")
        b = int(input("\n Enter a number: "))
        # get a middle element
        middle_element = a[int(len(a) / 2)]
        print("This is a middle element of list a: ", middle_element)

        if b == middle_element:
            print(b, " is in the list! #first check")

        elif b <= middle_element:

            # create a half list

            new_list = []
            for x in a:
                if x < middle_element:
                    new_list.append(x)
                else:
                    pass
            print("This is a new list with left smaller numbers: ", new_list)

            # get a middle element form a half list

            middle_element_2 = new_list[int(len(new_list) / 2)]
            print("This is a new middle element: ", middle_element_2)
            if b == middle_element_2:
                print(b, " is in the list!# in the second check for smaller numbers")

            elif b <= middle_element_2:
                # create a shorter list
                third_list = []
                for x in new_list:
                    if x < middle_element_2:
                        third_list.append(x)
                    else:
                        pass
                print("This is a new list with left smaller numbers: ", third_list)
                # compare/ find

                if b in third_list:
                    print("The left list has your number: ", b)
                else:
                    print("The left list hasn't got your number.")

            else:
                # create a shorter list
                third_list = []
                for x in new_list:
                    if x > middle_element_2:
                        third_list.append(x)
                    else:
                        pass
                print("This is a new list with left smaller numbers: ", third_list)
                # compare/ find

                if b in third_list:
                    print("The left list has your number: ", b)
                else:
                    print("The left list hasn't got your number.")

        # variant for numbers bigger from middle value

        else:
            # create a half list
            bigger_third_list = []
            new_list2 = []
            for x in a:
                if x > middle_element:
                    new_list2.append(x)
                else:
                    pass
            print("This is a new list with RIGHT BIGGER numbers: ", new_list2)

            # get a middle element form a half list

            bigger_middle_element_2 = new_list2[int(len(new_list2) / 2)]
            print("This is a new middle element: ", bigger_middle_element_2, "of your new list: ", new_list2)

            if b == bigger_middle_element_2:
                print(b, " is in the list!# in the second check for bigger numbers")

            elif b <= bigger_middle_element_2:
                # create a shorter list
                # bigger_third_list = []
                for x in new_list2:
                    if x < bigger_middle_element_2:
                        bigger_third_list.append(x)
                    else:
                        pass
                        # compare/ find
                print("This is your new list: ", bigger_third_list)

                if b in bigger_third_list:
                    print("The right list has your number: ", b)
                else:
                    print("The right list hasn't got your number.")
            else:

                # create a shorter list
                # bigger_third_list = []
                for x in new_list2:
                    if x > bigger_middle_element_2:
                        bigger_third_list.append(x)
                    else:
                        pass
            # compare/ find
                print("This is your new list: ", bigger_third_list)

                if b in bigger_third_list:
                    print("The right list has your number: ", b)
                else:
                    print("The right list hasn't got your number.")


if __name__ == '__main__':
    binary_search()
"""


def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    print("last: ", last)
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        print("mid: ", mid)
        if item_list[mid] == item:
            print("item_list[mid]: ", item_list[mid])
            found = True

        else:
            if item < item_list[mid]:
                last = mid - 1
                print("else, if item: ", item )
                print("else if item list: ",item_list)
            else:
                first = mid + 1
    return found

print(binary_search([1, 2, 3, 5, 8], 6))
#print(binary_search([1, 2, 3, 5, 8], 5))