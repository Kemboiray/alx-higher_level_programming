#!/usr/bin/python3

# 8-multiple_returns.py
def multiple_returns(sentence):
    '''
    Returns a tuple consisting of the length of a string
    and its first character (which is set to `None` in the
    case of an empty string)

    Args:
        `sentence`: string
    '''
    str_len = len(sentence)
    if str_len == 0:
        return (str_len, None)
    else:
        return (str_len, sentence[0])
