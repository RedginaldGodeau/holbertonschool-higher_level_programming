#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    for arg in range(len(args)):
        print("{:}: {:}".format(arg, args[arg])) 
