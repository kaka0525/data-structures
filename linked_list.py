class Node(object):
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer

    def get_data(self):
        return self.data

    def get_next(self):
        return self.pointer

    def set_next(self, new_next):
        self.pointer = new_next


class LinkList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        """ will insert the value 'val' at the head of the list"""
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        """will pop the first value off the head of the list and return it"""
        current = self.head
        return current
        self.head = current.get_next()

    def size(self):
        """will return the length of the list"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, val):
        """
        will return the node containing 'val' in the list, if present,
        else None

        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == val:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def remove(self, node):
        """
        will remove the given node from the list, wherever it might be
        (node must be an item in the list
        """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == node:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def display(self):
        """will print the list represented as a Python tuple literal:
        "(12, 'sam', 37, 'tango')
            bonus if you can make it so that the list appears this way on its
            own (remember special methods)."""
        pass
