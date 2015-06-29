# _*_ coding: utf-8- _*_


class Node(object):
    def __init__(self, val=None, pointer=None):
        self.val = val
        self.pointer = pointer


class Queue(object):
    def __init__(self, head=None, prev=None):
        self.head = head
        self.prev = prev
        self.size_ = 0

        def enqueue(self, val):
            node = Node(val)
            pass

        def dequeue(self):
            pass

        def size(self):
            return self.size_


"""
1. enqueue(value): adds value to the queue
2. dequeue(): removes the correct item from the queue and returns its value
    (should raise an error if the queue is empty)
3. size(): return the size of the queue.  Should return 0 if the queue is
    empty.
"""
