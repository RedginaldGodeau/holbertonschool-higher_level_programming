#!/usr/bin/python3
"""_summary_"""
import json

class Base:
    """_summary_"""

    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (list / dict): List of element in class

        Returns:
            json: encode in json
        """
        data = []
        if isinstance(list_dictionaries, (list, dict)):
            data = json.dumps(list_dictionaries)
        return data

    @classmethod
    def save_to_file(cls, list_objs):
        for i in range(len(list_objs)):
            if isinstance(list_objs[i], Base):
                list_objs[i] = list_objs[i].to_dictionary()
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            data = cls.to_json_string(list_objs)
            f.write(data)

    @classmethod
    def create(cls, **dictionary):
        new = cls(1, 1)
        new.update(**dictionary)
        return new
    @classmethod
    def load_from_file(cls):
        data = []
        with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
            data = cls.from_json_string(f.read())
            if isinstance(data, list):
                for i in range(len(data)):
                    data[i] = cls.create(data[i])
        return data

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return None
        return json.loads(json_string)
