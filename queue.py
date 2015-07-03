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
        self._size = 0

    def enqueue(self, val):
        """
        Insert new Node at the back of the queue. If queue is empty, first Node
        becomes Front of queue. Otherwise, new Nodes are added to back of
        queue.
            arg:
                val: Value associated as the data of the Node
        """
        node = Node(val)
        self.back = node
        self._size += 1

        if self.front is None:
            self.front = node
        else:
            node = Node(val)
            self.back.next_node = node

    def dequeue(self):
        """
        Remove Node from Front of queue, and assign next Node in line as
        Front of queue.
        """
        # Write a test to verify the fix for self.back.
        current = self.front
        if self._size > 0:
            self._size -= 1
        if not current:
            self.back = None
            # Back pointer needs to be removed when current.next node is None
            raise IndexError("Queue is empty")
        self.front = current.next_node
        return current.val

    def size(self):
        """Return the current amount of Nodes in the queue as size"""
        return self._size
