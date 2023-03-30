#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers

    Arg my_list: list of elements
    Arg x: number of elements
    Return: Real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            count += 1
    if count:
        print()
    return count
