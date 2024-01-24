#!/usr/bin/python3
"""Defination of a class Square."""


class Square:
    """
        defines a square by size.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize a square
            Args:
                size (int): the size of the square.
                position (int, int): the position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print("")

    @property
    def size(self):
        """to retrive the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
