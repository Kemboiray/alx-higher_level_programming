#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]
            elem_new = elem_1 / elem_2
        except ZeroDivisionError:
            elem_new = 0
            print('division by 0')
        except TypeError:
            elem_new = 0
            print('wrong type')
        except IndexError:
            elem_new = 0
            print('out of range')
        finally:
            new_list.append(elem_new)
    return new_list
