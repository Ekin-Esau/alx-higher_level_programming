#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv[1:])
    args = sys.argv[1:]

    if args == 0:
        print("{} arguments.".format(num_args))
    elif args == 1:
        print("{} argument:".format(num_args))
    else:
        print("{} arguments:".format(num_args))
    
    for arg in range(num_args):
        print("{}: {}".format(arg + 1, sys.argv[arg + 1]))
