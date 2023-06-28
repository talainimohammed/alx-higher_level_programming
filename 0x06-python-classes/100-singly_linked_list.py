#!/usr/bin/python3

"""No Module"""


class Node:
    """
    Node class
    """
    def __init__(self, data, next_node=None):
        if self.__validate_data(data):
            self.__data = data
        if self.__validate_node(next_node):
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if self.__validate_data(value):
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if self.__validate_node(value):
            self.__next_node = value

    def __validate_data(self, data):
        if isinstance(data, int):
            return True
        return False

    def __validate_node(self, node):
        if isinstance(node, Node) or node is None:
            return True
        return False


class SinglyLinkedList:
    """
    contains nodes
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        tp = self.__head
        string = ""
        while tp is not None:
            string += str(tp.data)
            tp = tp.next_node
            if tp is not None:
                string += '\n'
        return string

    def sorted_insert(self, value):
        tp = self.__head
        if tp is None:
            self.__head = Node(value)
            return

        prev = None
        while tp is not None:
            if (tp.next_node is None or tp.next_node.data >= value):
                if (tp.data >= value):
                    next_n = tp
                    tp = Node(value)
                    tp.next_node = next_n
                    if prev is not None:
                        prev.next_node = tp
                    else:
                        self.__head = tp
                else:
                    next_n = tp.next_node
                    tp.next_node = Node(value)
                    tp.next_node.next_node = next_n
                return

            prev = tp
            tp = tp.next_node
