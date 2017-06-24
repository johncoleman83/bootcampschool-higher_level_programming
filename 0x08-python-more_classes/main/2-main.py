#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

a_rectangle = Rectangle(0, 4)
print("Area: {} - Perimeter: {}".format(a_rectangle.area(), a_rectangle.perimeter()))

print("--")

a_rectangle.width = 1
a_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(a_rectangle.area(), a_rectangle.perimeter()))
