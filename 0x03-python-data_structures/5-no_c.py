#!/usr/bin/python3

# 5-no_c.py
def no_c(my_string):
    '''
    removes all characters c and C from a string
    '''
    my_list = []
    for i in my_string:
        if i not in ('C', 'c'):
            my_list.append(i)
    new_string = my_list[0]
    for i in range(1, len(my_list)):
        new_string += my_list[i]
    return new_string
