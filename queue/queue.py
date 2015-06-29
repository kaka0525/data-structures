# _*_ coding: utf-8- _*_
from __future__ import unicode_literals


class Node(object):
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node


class Queue(object):
    def __init__(self, back=None, front=None):
        self.back = back
        self.front = front
        self.size_ = 0

    def enqueue(self, val):
        if self.front is None:
            node = Node(val)
            self.front = node
            self.back = node
            self.size_ += 1
        else:
            node = Node(val)
            self.back.next_node = node
            self.back = node
            self.size_ += 1

    def dequeue(self):
        current = self.front
        self.front = current.next_node
        current.next_node = None
        self.size_ -= 1

    def size(self):
        return self.size_


"""
1. enqueue(value): adds value to the queue
2. dequeue(): removes the correct item from the queue and returns its value
    (should raise an error if the queue is empty)
3. size(): return the size of the queue.  Should return 0 if the queue is
    empty.
"""
