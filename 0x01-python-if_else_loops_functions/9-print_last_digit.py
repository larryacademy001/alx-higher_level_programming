#!/usr/bin/python3

# print_last_digit - prints the last digit of a number.
# number: decimal input.
# Return - Last digit of number
def print_last_digit(number):
    if number < 0:
        number *= -1
    if number > 9:
        number %= 10
    print(number, end="")
    return number
