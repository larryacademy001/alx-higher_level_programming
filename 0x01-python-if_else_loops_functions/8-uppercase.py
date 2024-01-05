#!/usr/bin/python3

# uppercase - prints a string in uppercase followed by a new line.
# str: string input.
# Return - Nothing.
def uppercase(str):
    mod = str + "\n"
    for c in mod:
        if (ord(c) > (ord('a')-1)) and (ord(c) < (ord('z') + 1)):
            c = chr(ord(c) - (ord("a") - ord("A")))
        print("{}".format(c), end="")
