#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ This is a Rectangle Class (it defines a rectangle) """
    def __init__(self, width=0, height=0):
        """ Instantiation of rectangle with width and height """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns width of Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width of Rectangle """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ returns height of Rectangle """
        return self.__height

    @width.setter
    def height(self, value):
        """ sets height of Rectangle """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area of Rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns perimeter of Rectangle """
        if self.__width == 0 or self.__height == 0:
            p = 0
        else:
            p = self.__width * 2 + self.__height * 2
        return p
