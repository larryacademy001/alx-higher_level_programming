#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for char in my_list:
        if char == 'c' or c == 'C':
            my_list.remove(char)
    return("".join(my_list))
