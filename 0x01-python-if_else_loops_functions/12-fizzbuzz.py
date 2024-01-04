#!/usr/bin/python3

# fizzbuzz - prints the numbers from 1 to 100 separated by a space.
#            For multiples of three print Fizz instead of the number
#            and for multiples of five print Buzz.
#            For numbers which are multiples of both three and five
#            print FizzBuzz.
#
# Return - Nothing.
def fizzbuzz():
    for i in range(1, 101, 1):
        if (i % 15 == 0):
            print('FizzBuzz', end=" ")
        elif (i % 3 == 0):
            print('Fizz', end=" ")
        elif (i % 5 == 0):
            print('Buzz', end=" ")
        else:
            print(i, end=" ")
