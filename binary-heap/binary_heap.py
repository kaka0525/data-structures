#  encode
from __future__ import unicode_literals


class MinBinaryHeap(object):
    def __init__(self, values=None):
        self.heap_list = []
        if values is not None:
            for value in values:
                if type(value) is not int:
                    raise TypeError("That is not a number value")
                self.push(value)

    def push(self, val):
        """
        Puts a new value into the heap, maintaining the heap property.
        """
        self.heap_list.append(val)


    def pop(self):
        """
        Removes the "top" value in the heap, maintaining the heap property.
        """
        pass
