from linked_list import LinkedList


class Stack(object):
    def __init__(self):
        self.ll = LinkedList()

    def push(self, val):
        self.ll.insert(val)

    def pop(self):
        self.ll.pop()
