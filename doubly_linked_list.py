# _*_ coding: utf-8- _*_
from __future__ import unicode_literals


class Node(object):
    def __init__(self, val=None, next_node=None, prev=None):
        self.val = val
        self.next_node = next_node
        self.prev = prev


class Doublylinkedlist(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        """ Insert the value 'val' at the head of the list"""
        new_node = Node(val)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev = new_node

        self.head = new_node

    def append(self, val):
        """Append the value 'val' at the tail of the list"""
        new_node = Node(val)
        current = self.tail
        if current is None:
            self.head = new_node
            new_node.next_node, new_node.prev = new_node
        else:
            current.prev = new_node
            new_node.next_node = current

        self.tail = new_node

    def pop(self):
        """Pop the first value off the head of the list and return it"""
        if self.head is None:
            raise AssertionError("There is nothing to pop")
        else:
            pop_value = self.head.val
            self.head = self.head.next_node
            return pop_value

    def shift(self):
        """Remove the tail value from the tail of the list and return it"""
        current = self.tail
        if self.tail is None:
            raise ValueError("The list is empty")
        elif self.head is current:
            self.head = self.tail = None
        else:
            current.prev.next_node = None
            self.tail = self.tail.prev
        return current.val

    def remove(self, val=None):
        """
        Remove the head instance of 'val' found in the list, starting from
        the head. If 'val' is nor present, it will raise an appropriate
        python exception
        """
        if not val:
            raise ValueError("You must provide a Node Value")
        if self.head is None:
            raise AttributeError("The list is empty")
        else:
            current = self.head
            while current.val != val:
                if current.next_node is None:
                    raise ValueError("Value not found in list")
                else:
                    current = current.next_node
            if current.prev is None:
                self.head = self.head.next_node
            else:
                current.prev.next_node = current.next_node
                current.next_node.prev = current.prev
