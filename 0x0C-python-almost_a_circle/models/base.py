#!/usr/bin/python3
"""module for base class
"""


import turtle


class Base:
    """base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string of list_dictionaries
        """
        return str(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionary
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return eval(json_string)

    @staticmethod
    def to_csv_lines(list_csv):
        """returns CSV string
        """
        build = ""
        for csv in list_csv:
            for i, ele in enumerate(csv):
                build += str(ele)
                if i != len(csv) - 1:
                    build += ','
            build += '\n'
        return build

    @staticmethod
    def from_csv_lines(list_csv):
        """returns list of CSV
        """
        if list_csv is None or len(list_csv) == 0:
            return []

        csv_dt = []
        for line in list_csv:
            raw_data = line.strip('\n').split(',')
            csv_dt.append([int(ele) for ele in raw_data])
        return csv_dt

    @staticmethod
    def get_cname_from_sublist(list_objs):
        """gets proper cn
        """
        cn = None
        for i, obj in enumerate(list_objs):
            if not issubclass(type(obj), Base):
                continue
            elif cn is None or cn != "Rectangle":
                cn = obj.__class__.__name__
        if cn is None:
            cn = "Rectangle"
        return cn

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objects
        """
        new_list = None
        list_obj_cp = list_objs.copy()
        cn = cls.get_cname_from_sublist(list_obj_cp)

        super_l = []
        for ele in list_obj_cp:
            if issubclass(type(ele), Base):
                super_l.append(ele.to_dictionary())
        write_str = cls.to_json_string(super_l)
        with open(cn + '.json', 'w', encoding='utf-8') as myFile:
            myFile.write(write_str)

    @classmethod
    def create(cls, **dictionary):
        """creates a new instance of sub class
        """
        new_instance = cls(1, 1)
        if new_instance is not None:
            new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of all instances
        """
        cn = cls.__name__
        try:
            with open(cn + '.json', 'r', encoding='utf-8') as myFile:
                text = myFile.read()
        except Exception:
            return []

        inst_l = []
        dict_list = cls.from_json_string(text)
        for ele in dict_list:
            inst_l.append(cls.create(**ele))
        return inst_l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of sub-class
        """
        list_obj_cp = list_objs.copy()
        # get_cname_from_sublist also removes non subclass eles, so copy
        cn = cls.get_cname_from_sublist(list_obj_cp)
        super_l = []

        for ele in list_obj_cp:
            if issubclass(type(ele), Base):
                super_l.append(ele.to_csv())
        write_str = cls.to_csv_lines(super_l)
        with open(cn + '.csv', 'w', encoding='utf-8') as myFile:
            myFile.write(write_str)

    @classmethod
    def load_from_file_csv(cls):
        """loads a list of objects
        """
        cn = cls.__name__
        try:
            with open(cn + '.csv', 'r', encoding='utf-8') as myFile:
                lines = myFile.readlines()
        except Exception:
            return []

        inst_l = []
        csv_list_list = cls.from_csv_lines(lines)
        for csv_inst in csv_list_list:
            new_obj = cls(1, 1)
            new_obj.update(*csv_inst)
            inst_l.append(new_obj)
        return inst_l

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws the rectangles
        """
        window = turtle.Screen()
        window.bgcolor("green")
        all_eles = list_rectangles.copy()
        all_eles.extend(list_squares)
        turtles = [turtle.Turtle() for ele in all_eles]
        for i, t in enumerate(turtles):
            if i < len(list_rectangles):
                t.color("blue")
                if i > 0:
                    prev_pos = turtles[i - 1].position()
                    prev_x = prev_pos[0] + list_rectangles[i - 1].width
                    pre_y = prev_pos[1]
                    if i % 6 == 0:
                        pre_y = prev_pos[1] + list_rectangles[i - 1].height
                    t.setpos(prev_x, pre_y)
                t.forward(list_rectangles[i].width)
                t.right(90)
                t.forward(list_rectangles[i].height)
                t.right(90)
                t.forward(list_rectangles[i].width)
                t.right(90)
                t.forward(list_rectangles[i].height)
            else:
                t.color("red")
                if i > 0:
                    cur_sq_i = i - len(list_rectangles)
                    prev_pos = turtles[i - 1].position()
                    prev_x = prev_pos[0] + list_squares[cur_sq_i - 1].size
                    prev_y = prev_pos[1]
                    if i % 6 == 0:
                        prev_y = prev_pos[1] + list_squares[cur_sq_i - 1].size
                    t.setpos(prev_x, prev_y)
                for s in range(0, 4):
                    t.forward(list_squares[cur_sq_i].size)
                    t.right(90)
