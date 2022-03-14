# -*- coding: utf-8 -*-
import os
import sys


def add_python_path():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


def print_python_path():
    for i in sys.path:
        print(i)


if __name__ == '__main__':
    if sys.argv[1] == 'add_python_path':
        add_python_path()
    elif sys.argv[1] == 'print_python_path':
        print_python_path()
    else:
        print('you can add only one parameter')
        exit()
