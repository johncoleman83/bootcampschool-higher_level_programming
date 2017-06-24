#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("{} - {}".format(my_rectangle.width, my_rectangle.height))
my_rectangle.width = 10
print("{} - {}".format(my_rectangle.width, my_rectangle.height))
