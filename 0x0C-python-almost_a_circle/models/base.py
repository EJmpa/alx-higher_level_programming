#!/usr/bin/python3
import json
import os
import csv

"""This module stores a class named `'Base'`"""

class Base:
    """A Python class - 'Base' for evaluation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """An dunder method(__init__()) for
        initializing `'Base'` class arguments
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the `JSON string` representation of `'list_dictionaries'`"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `'list_objs'` to a file"""
        filename = cls.__name__+'.json'
        try:
            jsons = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            jsons = '[]'
        with open(filename, 'w', encoding='utf-8') as json_file:
            json_file.write(jsons)
        
        
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation `'json_string'`"""
        if json_string is not None or len(json_string) != 0:
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            return json.loads(json_string)
        
        else:
            return list()
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Square':
            dummy = cls(1)
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if dummy:
            dummy.update(**dictionary)
            return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        elif os.path.exists:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**dic) for dic in list_dicts]
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    objs.append(obj)
                return objs
        except FileNotFoundError:
            return []
