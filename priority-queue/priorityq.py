# _*_ coding: utf-8- _*_
from binary_heap import MinBinaryHeap


class PriorityQ(object):
    def __init__(self):
        self.priorities = {}
        self._order = 1

    def _create_priorities(self, pri):
        """Create new Heap based on priority argument"""
        heaps = self.priorities
        heaps[pri] = MinBinaryHeap()

    def _check_priority(self):
        pass

    def insert(self, pri):
        """

        """
        heaps = self.priorities
        if pri > 10 or pri < 1:
            raise ValueError(
                'Priority must be between 1 (high) - 10 (low)'
            )
        if pri not in heaps.keys():
            self._create_priorities(pri)

        priority = heaps.get(pri)
        priority.push(self._order)
        self._order += 1

    def pop(self):
        """

        """

        def sub_pop():
            heaps = self.priorities
            keys = heaps.keys()
            keys = min(keys)
            heap = heaps[keys]
            pop = heap.pop()
            return pop

        def remove_key():
            heaps = self.priorities
            keys = heaps.keys()
            keys = min(keys)
            heaps.pop(keys)

        try:
            val = sub_pop()
        except IndexError:
            remove_key()
            val = sub_pop()

        return val

    def peek(self):
        """
        Checks to see what the most important item in the queue is,
        and returns that value without removing it.
        """
        pass
