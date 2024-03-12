#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    i = 0
    j = 0
    new_str = []
    while (i < len(str) - 1):
        if i == n:
            j += 1
        new_str[i] = str[j]
        i += 1
        j += 1
    return new_str
