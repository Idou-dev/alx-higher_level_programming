#!/usr/bin/python3
import sys
i = 1
a = len(sys.argv)
while(i <= a):
    if a < 2:
        print("0 arguments.")
    elif a == 2:
        print("{:d} argument:".format(a))
        print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print("{:d} arguments:".format(a))
        print("{:d}: {}".format(i, sys.argv[i]))
    i += 1
