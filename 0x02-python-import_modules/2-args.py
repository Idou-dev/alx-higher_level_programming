#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv)
    i = 1
    if j < 2:
        print("{} {}".format(j - 1, "arguments."))
    elif j == 2:
        print("{} {}".format(i, "argument:"))
        while (i < j):
            print("{}: {}".format(j - 1, sys.argv[i]))
            i += 1
    else:
        print("{} {}".format(j - 1, "arguments:"))
        while (i < j):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
