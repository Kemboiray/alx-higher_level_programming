#!/usr/bin/python3

def safe_print_division(a, b):
    """
    print the division of integer a with integer b

    Return: dividend or None (error)
    """
    try:
        c = a / b
    except Exception:
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
