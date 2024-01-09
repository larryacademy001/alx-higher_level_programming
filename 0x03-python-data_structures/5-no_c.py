#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for c in my_list:
        if c == 'c' or c == 'C':
            my_list.remove(c)
    return("".join(my_list))
