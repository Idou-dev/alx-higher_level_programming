#!/usr/bin/python3
i = 122
while (i > 96):
    if i % 2 != 0:
        j = chr(i - 32)
    else:
        j = chr(i)
    print("{}".format(j), end="")
    i -= 1
