#!/usr/bin/python3
def uppercase(str):
    for d in str:
        d = ord(d)
        if d > 96 and d < 123:
            d -= 32
        print("{}".format(chr(d)), end="")
    print()
