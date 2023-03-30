#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element-wise

    Return: new list of dividends
    """
    new_list = list()
    for i in range(list_length):
        try:
            d = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            break
        else:
            new_list.append(d)
    return new_list
