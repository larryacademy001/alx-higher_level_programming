#!/usr/bin/python3
# 3-infinite_add.py
# program that prints the result of the addition of all arguments

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total_sum = 0
    for i in range(len(sys.argv) - 1):
        total_sum += int(sys.argv[i + 1])
    print("{}".format(total_sum))
