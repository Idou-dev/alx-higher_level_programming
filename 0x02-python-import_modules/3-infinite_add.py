#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    i = 1
    while (i < len(sys.argv)):
        add = add + int(sys.argv[i])
        i += 1
    print("{}".format(add))
