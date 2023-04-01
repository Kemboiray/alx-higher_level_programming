#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list skipping non-integers

    Arg my_list: given list
    Arg x: number of elements to print

    Return value: Number of elements printed.
    """
    count = 0
    for i in range(x):
        elem = my_list[i]
        try:
            if not isinstance(elem, int):
                pass
            else:
                print("{:d}".format(elem), end="")
                count += 1
        except ValueError:
            print()
            return count
    print()
    return count
