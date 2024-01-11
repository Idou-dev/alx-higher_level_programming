#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    i = 1
    if l < 2:
        print("{} {}".format(l - 1, "arguments."))
    elif l == 2:
        print("{} {}".format(i, "argument:"))
        while(i < l):
            print("{}: {}".format(l - 1, sys.argv[i]))
            i += 1
    else:
        print("{} {}".format(l - 1, "arguments:"))
        while(i < l):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
