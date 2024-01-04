#!/usr/bin/python3

# remove_char_at: creates a copy of the string,
#                 removing the character at the position n.
# str: the string.
# n: the index.
# Return: a modified string
def remove_char_at(str, n):
    if (n < 0):
        return str
    mod = str[0:n] + str[(n + 1):]
    return mod
