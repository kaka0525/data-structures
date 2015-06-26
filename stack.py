from linked_list import LinkList


class Stack(object):
    def __init__(self, top=None):
        self.top = top
        self.ll = LinkList()

    def push(self, val):
        self.ll.insert(val)
        self.top = self.ll.head

    def pop(self):
        self.ll.pop()
        self.top = self.ll.head
        return self.top.val
