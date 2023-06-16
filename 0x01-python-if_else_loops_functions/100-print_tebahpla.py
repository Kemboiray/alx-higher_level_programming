#!/usr/bin/python3

ascii_list = [122, 89, 120, 87, 118, 85, 116, 83, 114, 81, 112, 79, 110, 77,
              108, 75, 106, 73, 104, 71, 102, 69, 100, 67, 98, 65]
for num in ascii_list:
    print('{}'.format(chr(num)), end='')
