class Node(object):
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Doublylinkedlist(object):
    def __init__(self):
        self.head = None
        self.tail = None


        def insert(val):
            """ Insert the value 'val' at the head of the list"""
            new_node = Node(val)
            Dummy.next = new_node
            self.head = new_node


        def append(val):
            """Append the value 'val' at the tail of the list"""
            pass

        def pop():
            """Pop the first value off the head of the list and return it"""
            pass

        def shift():
            """Remove the last value from the tail of the list and return it"""
            pass

        def remove(val):
            """
            Remove the first instance of 'val' found in the list, starting from
            the head. If 'val' is nor present, it will raise an appropriate
            python exception
            """
            pass



