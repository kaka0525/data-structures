class Node(object):
    def __init__(self, val=None, pointer=None):
        self.val = val
        self.pointer = pointer


class LinkedList(object):
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
                val: Value associated with the val property of Node
        """
        current = self.size()
        next_node = self.head
        for num in range(current):
            if next_node.val == val:
                return next_node
            next_node = next_node.pointer
        return None

    def display(self):
        """Display the current Nodes in the list as a string representation
        of a tuple type"""
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
                node_val: Value associated with the val property of Node
        """
        current = self.head
        rem_node = self.search(node_val)
        while current is not None:
            if current.pointer is rem_node:
                current.pointer = rem_node.pointer
                self.size_ -= 1
            else:
                current = current.pointer

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
            raise IndexError("Stack is empty")
        self.head = current.pointer
        self.size_ -= 1
        return self.size()
