#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    n = len(argv)
    if n == 2:
        print('{} argument:'.format(1))
    elif n > 2:
        print('{} arguments:'.format(n - 1))
    else:
        print('{} arguments.'.format(0))
    for i in range(1, n):
        print('{}: {}'.format(i, argv[i]))
