#!/usr/bin/python3
for letter in range(97, 123, 1):
    if chr(letter) == "q" or chr(letter) == "e":
        continue
    print("{}".format(chr(letter)), end="")
