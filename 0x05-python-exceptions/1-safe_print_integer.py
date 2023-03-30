#!/usr/bin/python3

def safe_print_integer(value):
    """
    prints an integer with "{:d}".format()

    Arg value: object to print

    Return: True (success), or False (failure)
    """
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
