#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]

    print("{:} arguments:".format(len(args)))
    for arg in range(len(args)):
        print("{:}: {:}".format(arg + 1, args[arg])) 
