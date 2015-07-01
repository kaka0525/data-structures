#  encode
from __future__ import unicode_literals
from math import ceil


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
        current = self.heap_list
        current.append(val)
        p_index = 0
        if len(current) > 2:
            idx = current.index(val)
            p_index = int(ceil((idx / 2.0) - 1))
            while val < current[p_index]:
                current[idx], current[p_index] = current[p_index], current[idx]
                idx = p_index
                # p_index = int(ceil((idx / 2.0) - 1))
        else:
            if len(current) is 2:
                if current[0] > current[1]:
                    current[0], current[1] = current[1], current[0]
            else:
                return current
        return current

    def pop(self):
        """
        Removes the "top" value in the heap, maintaining the heap property.
        """
        pass
