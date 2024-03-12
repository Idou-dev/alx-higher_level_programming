#!/usr/bin/python3
size = input("How tall is the tree: ")
i = 1
size = int(size)
while(i <= size):
    for k in range(size - i):
        print(" ", end='')
    for j in range(i * 2 - 1):
        print("#", end='')
    for l in range(size - i):
        print(" ", end='')
    print()
    i += 1
