#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        for key in a_dictionary:
            best = sorted(a_dictionary.values(), reverse=True)[0]
            if a_dictionary[key] == best:
                return key
    else:
        return None
