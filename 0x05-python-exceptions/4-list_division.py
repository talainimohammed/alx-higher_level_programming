#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    j = 0
    new_l = []
    res = 0
    for j in range(0, list_length):
        try:
            res = (my_list_1[j] / my_list_2[j])
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_l.append(res)
    return new_l
