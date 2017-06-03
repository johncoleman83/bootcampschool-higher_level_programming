#!/usr/bin/python3
class Student():
    """Student class with name and age"""
    def __init__(self, first_name, last_name, age):
        """initializes new instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dict attributes of Student"""
        if attrs is None:
            obj_dict = self.__dict__
            return obj_dict
        else:
            o_D = self.__dict__
            D = dict(([k, v] for k, v in o_D.items() if k in attrs))
            return D

    def reload_from_json(self, json):
        """reloads Student instance from input dictionary"""
        for k, v in json.items():
            setattr(self, k, v)
