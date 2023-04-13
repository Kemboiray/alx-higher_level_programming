#!/usr/bin/python3
"""Adds all arguments to a Python list, and saves them to a file,
`add_item.json`"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_obj = load_from_json_file('add_item.json')
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], 'add_item.json')
else:
    my_obj.extend(sys.argv[1:])
    save_to_json_file(my_obj, 'add_item.json')
