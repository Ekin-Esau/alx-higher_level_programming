#!/usr/bin/python3

    import sys

    num_args = len(sys.argv) - 1
    args = sys.argv[1:]

    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    for arg in range(num_args):
        print("{}: {}".format(arg + 1, sys.argv[arg + 1]))
