#!/usr/bin/python3
MyClass = __import__('10-my_class_2').MyClass
class_to_json = __import__('10-class_to_json').class_to_json

f = MyClass()
fj = class_to_json(f)
print(f)
print(fj)
