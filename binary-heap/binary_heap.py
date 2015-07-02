#  encode
from __future__ import unicode_literals


def _get_parent_index(i):
    return (i - 1) / 2


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
        hlist = self.heap_list
        hlist.append(val)
        val_index = len(hlist) - 1
        p_index = _get_parent_index(val_index)
        while val_index > 0:
            if hlist[p_index] > hlist[val_index]:
                (hlist[p_index], hlist[val_index]) = (hlist[val_index],
                                                      hlist[p_index])
                val_index = p_index
                p_index = _get_parent_index(val_index)
            else:
                break

    def _swap_nodes(self, a_index, b_index):
        hlist = self.heap_list
        (hlist[a_index], hlist[b_index]) = (hlist[b_index],
                                            hlist[a_index])

    def pop(self):
        hlist = self.heap_list
        if len(hlist) == 0:
            raise IndexError("The heap is empty")
        else:
            return_val = hlist[0]
            hlist[0] = hlist[-1]
            del hlist[-1]
            max_index = len(hlist) - 1
            current_index = 0
            while True:
                left_child_index = _get_left_child_index(current_index)
                right_child_index = _get_right_child_index(current_index)

                if left_child_index > max_index:
                    break
                elif (right_child_index > max_index and
                        hlist[left_child_index] < hlist[current_index]):
                    self._swap_nodes(current_index, left_child_index)
                    break
                elif (hlist[left_child_index] <= hlist[right_child_index] and
                        hlist[left_child_index] < hlist[current_index]):
                    self._swap_nodes(current_index, left_child_index)
                    current_index = left_child_index
                elif (hlist[right_child_index] < hlist[left_child_index] and
                        hlist[right_child_index] < hlist[current_index]):
                    self._swap_nodes(current_index, right_child_index)
                    current_index = right_child_index
                else:
                    break
            return return_val
