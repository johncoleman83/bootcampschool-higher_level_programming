#!/usr/bin/python3
"""module evaluate geometry using maths operations"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry class"""
    def __init__(self, width, height):
        """initializes new object of Rectangle Class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[{}] {:d}/{:d}".format("Rectangle", self.__width,
                                       self.__height)


class Square(Rectangle):
    """Square class inheriting from Rectangle class"""
    def __init__(self, size):
        """initializes new object of Rectangle Class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
