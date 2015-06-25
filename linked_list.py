class Node(object):
    def __init__(self, val=None, pointer=None):
        self.val = val
        self.pointer = pointer
        print(self.val, self.pointer)

    def get_info(self):
        """Return the argument value from Node constructor val perameter"""
        return self.val

    def next_node(self):
        """Return the value from the next Node in the list"""
        return self.pointer

    def set_next(self, next_n):
        """Assign the pointer value to the next Node in the list"""
        self.pointer = next_n


class LinkList(object):
    def __init__(self, head=None, **kwargs):
        self.head = head
        self.size = 0

    def size(self):
        """Return the current amount of Nodes in the list as size"""
        return self.size

    def search(self, val):
        """
        Find desired Node within list
            arg:
                val: String value associated with the val property of Node
        """
        current = self.head
        exists = False
        while current and exists is False:
            if current.get_info() == val:
                exists = True
            else:
                current = current.next_node()
        if not current:
            raise ValueError("That Node is not in this list")
        return current

    def display(self):
        """Display the current Nodes in the list as a tuple"""
        current = self.head
        output = ()
        while current:
            output += (current.val,)
            current = current.next_node()
        print(output)

    def remove(self, node):
        """
        Remove desired Node from list
            arg:
                node: String value associated with the val property of Node
        """
        self.size += 1
        current = self.head
        prev = None
        exists = False
        while current and exists is False:
            if current.get_info() == node:
                exists = True
            else:
                prev = current
                current = current.next_node()
            if not current:
                raise ValueError("That Node is not in this list")
            if not prev:
                self.head = current.next_node()
            else:
                prev.set_next(current.next_node())

    def insert(self, val):
        """
        Insert new Node at the front of the list, and assign new Node as Head
            arg:
                val: Value associated as the data of the Node
        """
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        """Remove first Node from list, and assign next Node as new Head"""
        current = self.head
        if not current:
            raise ValueError('There are no Nodes left in the list')
        self.head = current.next_node()
        self.size += 1
        return current.val
