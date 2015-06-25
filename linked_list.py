class Node(object):
    def __init__(self, val=None, pointer=None):
        self.val = val
        self.pointer = pointer
        print(self.val, self.pointer)

    def get_info(self):
        return self.val

    def next_node(self):
        return self.pointer

    def set_next(self, next_n):
        self.pointer = next_n

    # def __repr__(self):
    #     print(self.val)


class LinkList(object):
    def __init__(self, head=None, **kwargs):
        self.head = head
        self.size = 0

    def size(self):
        return self.size

    def search(self):
        pass

    def display(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next_node()

    def remove(self):
        self.size += 1
        pass

    def insert(self, val):
        """ will insert the value 'val' at the head of the list"""
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        """will pop the first value off the head of the list and return it"""
        current = self.head
        self.head = current.next_node()
        self.size += 1
        return current
