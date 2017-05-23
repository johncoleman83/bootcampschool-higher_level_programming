#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is a Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ instantiation of square with size & position """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if (type(position) != tuple or len(position) != 2
            or position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    @property
    def position(self):
        """ returns position variable of Square class instance """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets position variable of Square class instance """
        if (type(value) != tuple or len(value) != 2
            or value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ returns area of a square """
        return self.__size**2

    def my_print(self):
        """ prints a square of '#' """
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
        if self.__size == 0:
            print()
