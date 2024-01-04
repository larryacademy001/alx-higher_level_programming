#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
the_last_digit = abs(number)
while the_last_digit > 10:
    the_last_digit = the_last_digit % 10
if number < 0:
    the_last_digit = -the_last_digit
print("Last digit of {} is {} and is ".format(number, the_last_digit), end="")
if the_last_digit > 5:
    print("greater than 5")
elif the_last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
