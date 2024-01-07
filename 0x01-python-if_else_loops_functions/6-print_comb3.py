#!/usr/bin/python3
for n in range(1, 100):
    i = n // 10
    j = n % 10
    if i < j:
        print("{}{}".format(i, j), end="\n" if i == 8 else ", ")
