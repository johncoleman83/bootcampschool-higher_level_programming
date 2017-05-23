#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is a Square Class """
    def __init__(self, size=0):
        """ defining the size of square """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """ returns size variable of Square class instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size variable of Square class instance """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ returns area of a square """
        return self.__size**2

    def my_print(self):
        """ prints a square of '#' """
        for i in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print()
