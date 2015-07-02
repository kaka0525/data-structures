#  encode
from __future__ import unicode_literals
from math import ceil


def _get_left_child_index(i):
    return 2 * i + 1


def _get_right_child_index(i):
    return 2 * i + 2


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
            idx = len(current) - 1
            p_index = int(ceil((idx / 2.0) - 1))
            while val < current[p_index]:
                current[idx], current[p_index] = current[p_index], current[idx]
                idx = p_index
                if p_index > 1:
                    p_index = int(ceil((idx / 2.0) - 1))
                else:
                    p_index = 0
        else:
            if len(current) is 2.0:
                if current[0] > current[1]:
                    current[0], current[1] = current[1], current[0]
            else:
                return current
        return current

    def _swap_nodes(self, a_index, b_index):
        current = self.heap_list
        (current[a_index], current[b_index]) = (current[b_index],
                                                current[a_index])

    def pop(self):
        """
        Removes the "top" value in the heap, maintaining the heap property.
        """
        current = self.heap_list
        if len(current) == 0:
            raise IndexError("The heap is empty")
        else:
            return_val = current[0]
            current[0] = current[-1]
            del current[-1]
            max_index = len(current) - 1
            current_index = 0
            while True:
                left_child_index = _get_left_child_index(current_index)
                right_child_index = _get_right_child_index(current_index)

                if left_child_index > max_index:
                    break
                elif (right_child_index > max_index and
                        current[left_child_index] < current[current_index]):
                    self._swap_nodes(current_index, left_child_index)
                    break
                elif (current[left_child_index] <= current[right_child_index] and
                        current[left_child_index] < current[current_index]):
                    self._swap_nodes(current_index, left_child_index)
                    current_index = left_child_index
                elif (current[right_child_index] < current[left_child_index] and
                        current[right_child_index] < current[current_index]):
                    self._swap_nodes(current_index, right_child_index)
                    current_index = right_child_index
                else:
                    break
            return return_val
