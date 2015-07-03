# _*_ coding: utf-8- _*_
from binary_heap import MinBinaryHeap


class PriorityQ(object):
    def __init__(self):
        self.priorities = {}
        self._order = 1

    def _create_priorities(self, pri):
        """
        Create new Heap based on priority argument
            args:
                pri: This value will dictate the priority of the Heap,
                    in range of 1 (highest) to 10 (lowest).
        """
        heaps = self.priorities
        heaps[pri] = MinBinaryHeap()

    def _remove_key(self):
        """
        Remove empty Heap from the Priority Queue's dictionary.
        """
        heaps = self.priorities
        keys = heaps.keys()
        keys = min(keys)
        heaps.pop(keys)

    def insert(self, pri):
        """
        Insert new node into Heap, based on priority. The order of the insert
        is maintained by order dictating the value of the node in each Heap.
            args:
                pri: This value will dictate which Heap the node is placed in.
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
        Removes the highest priority node from the queue. If pop is called
        on an empty Heap, the empty Heap will be removed from the queue's
        collection.
        """

        def sub_pop():
            heaps = self.priorities
            keys = heaps.keys()
            keys = min(keys)
            heap = heaps[keys]
            pop = heap.pop()
            return pop

        try:
            val = sub_pop()
        except IndexError:
            self._remove_key()
            val = sub_pop()

        return val

    def peek(self):
        """
        Provide the return value of the highest priority node in the Queue
        without removing that value from the Queue.
        """
        heaps = self.priorities
        keys = heaps.keys()
        key = min(keys)
        heap = heaps[key]
        heap_list = heap.heap_list

        if len(heap_list) == 0:
            self._remove_key()
            keys = heaps.keys()
            key = min(keys)
            heap = heaps[key]
            heap_list = heap.heap_list

        return heap_list[0]
