class Node(object):
    def __init__(self, val=None, pointer=None):
        self.val = val
        self.pointer = pointer


class LinkList(object):
    def __init__(self, values=None, head=None):
        self.head = head
        self.size_ = 0
        if values is not None:
            for value in values:
                self.insert(value)

    def size(self):
        """Return the current amount of Nodes in the list as size"""
        return self.size_

    def search(self, val):
        """
        Find desired Node within list
            arg:
                val: String value associated with the val property of Node
        """
        current = self.head
        while current:
            if current.val == val:
                break
            else:
                current = current.pointer
        if not current:
            return None
        return current

    def display(self):
        """Display the current Nodes in the list as a tuple"""
        current = self.head
        output = "("
        while current is not None:
            if output != "(":
                output = "{},{}".format(output, repr(current.val))
            else:
                output += repr(current.val)
            current = current.pointer
        output += ")"
        return output

    def remove(self, node_val):
        """
        Remove desired Node from list
            arg:
                node_val: String value associated with the val property of Node
        """
        current = self.head
        next_node = self.head.pointer
        if current.val == node_val:
            self.head = self.head.pointer
            current.pointer = None
            self.size_ -= 1
        else:
            while next_node is not None:
                if next_node.val == node_val:
                    current.pointer = next_node.pointer
                    next_node.pointer = None
                    self.size_ -= 1
                    break
                else:
                    current = current.pointer
                    next_node = next_node.pointer

    def insert(self, val):
        """
        Insert new Node at the front of the list, and assign new Node as Head
            arg:
                val: Value associated as the data of the Node
        """
        new_node = Node(val, self.head)
        self.head = new_node
        self.size_ += 1

    def pop(self):
        """Remove first Node from list, and assign next Node as new Head"""
        current = self.head
        if not current:
            raise ValueError('There are no Nodes left in the list')
        self.head = current.pointer
        self.size_ -= 1
        return current.val
