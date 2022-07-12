#!/usr/bin/python3
for i in range(122, 96, -1):
    j = chr(i)
    if i % 2 != 0:
        j = j.upper()
    print("{}".format(j), end="")
