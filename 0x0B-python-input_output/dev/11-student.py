#!/usr/bin/python3
class Student():
    """Student class with name and age"""
    def __init__(self, first_name, last_name, age):
        """initializes new instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dict attributes of Student"""
        try:
            obj_dict = self.__dict__
            return obj_dict
        except:
            return {}
