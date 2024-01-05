#!/usr/bin/python3
# 0_add.py
# program that imports the function def add(a, b): 
# from the file add_0.py and prints the result of the 
# addition 1 + 2 = 3

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
