#!/usr/bin/python3
"""module evaluate geometry using maths operations"""


class BaseGeometry:
    """Geometry class with maths operations"""
    def __init__(self):
        """initializes new object of BaseGeometry Class"""
        pass

    def area(self):
        """defines area of shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if input:value is integer"""
        if (value.__class__ != int):
            raise TypeError("{:} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))


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
        return "[{}] {:d}/{:d}".format(type(self).__name__, self.__width,
                                       self.__height)


class Square(Rectangle):
    """Square class inheriting from Rectangle class"""
    def __init__(self, size):
        """initializes new object of Rectangle Class"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
