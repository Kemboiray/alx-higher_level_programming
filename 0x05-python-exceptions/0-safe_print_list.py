#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints x elements of a list, followed by a new line

    Arg my_list: list of elements
    Arg x: number of elements to print

    Return: Real number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
        print()
    except (IndexError, ValueError):
        print()
    return count
