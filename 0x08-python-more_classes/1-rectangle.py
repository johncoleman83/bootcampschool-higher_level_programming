#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ This is a Rectangle Class (it defines a rectangle) """
    def __init__(self, width=0, height=0):
        """ Instantiation of rectangle with width and height """
        self.width = width
        self.height = height

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

    @height.setter
    def height(self, value):
        """ sets height of Rectangle """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
