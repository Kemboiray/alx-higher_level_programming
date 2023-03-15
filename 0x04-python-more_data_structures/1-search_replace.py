#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        new = []
        for i in my_list:
            if i == search:
                new.append(replace)
            else:
                new.append(i)
        return new
