#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4
    ls = dir(hidden_4)
    for w in ls:
        if w[0] != '_':
            print('{}'.format(w))
