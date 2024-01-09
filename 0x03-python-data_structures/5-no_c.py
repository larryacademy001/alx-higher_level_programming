#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    i = 0
    while (i < len(my_string)):
        if not ((my_string[i] == 'c') or (my_string[i] == 'C')):
            new_string += my_string[i]
        i += 1
    return new_string
