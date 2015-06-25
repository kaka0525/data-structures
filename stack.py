from linked_list import LinkList, Node


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, val):
        ll = LinkList()
        top_ = ll.insert(val)
        self.top = top_

    def pop(self):
        pass
