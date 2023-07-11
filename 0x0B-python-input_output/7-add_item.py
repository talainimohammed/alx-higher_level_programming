#!/usr/bin/python3
"""module for taking arguments
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """contain main code
    """
    try:
        new_l = load_from_json_file('add_item.json')
    except:
        new_l = []

    new_l.extend([sys.argv[i] for j in range(0, len(sys.argv)) if j != 0])
    try:
        save_to_json_file(new_l, 'add_item.json')
    except:
        pass

main()
