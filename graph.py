# _*_ encode: utf-8 _*_
from __future__ import unicode_literals


class Graph(object):
    def __init__(self):
        self.g_dict = {}

    def __repr__(self):
        return "This graph's node values are {}".format(
            self.g_dict.keys()
        )

    def __getitem__(self, idx):
        return self.g_dict[idx]

    def nodes(self):
        """Return a list of all nodes in the Graph."""
        return self.g_dict.keys()

    def edges(self):
        """Return a list of all edges in the Graph.
            Provides a list of all key/value pairs within the Graph dict
        """
        for node in self.g_dict:
            for edge in self.g_dict[node]:
                print(node, edge)

    def add_node(self, val):
        """
        Add a new node, n, to the Graph.
            args:
                val: Val association for new node
        """
        if val not in self.g_dict.keys():
            self.g_dict[val] = []
        else:
            raise KeyError('That node already exists in the Graph')

    def add_edge(self, n1, n2):
        """
        Add a new edge connecting two nodes, n1 and n2, to the Graph.
        If either n1 or n2 do not exist, they will be added to the Graph.
            args:
                n1, n2: Vals association for nodes to be connected
        """
        try:
            self.g_dict[n1].append(n2)
        except KeyError:
            self.add_node(n1)
            self.g_dict[n1].append(n2)

    def del_node(self, val):
        """
        Delete node, val, from Graph.
            args:
                val: Val association for node to be deleted
        """
        try:
            self.g_dict.pop(val)
        except:
            raise KeyError(u'That node does not exist in Graph')

    def del_edge(self, n1, n2):
        """
        Delete edge connecting two nodes, n1 and n2, from Graph.
            args:
                n1, n2: Vals association for node connected to edge to
                be deleted
        """
        try:
            self.g_dict[n1].remove(n2)
        except:
            raise KeyError(u'That edge does not exist in Graph')

    def has_node(self, val):
        """Return Boolean value associated with the result of whether node,
        val, exists in Graph.
            args:
                val: Val association for node to be verified"""
        if val not in self.g_dict:
            return False
        else:
            return True

    def neighbors(self, val):
        """Return a list of all nodes connected by edges to the node, val,
        in the Graph.
            args:
                val: Val association for node"""
        if val not in self.g_dict:
            raise KeyError(u'That node does not exist in Graph')

        neighbor_list = []
        for node in self.g_dict:
            if val in self.g_dict[node]:
                neighbor_list.append(node)
        return neighbor_list

    def adjacent(self, n1, n2):
        """Return Boolean value associated with the result of whether nodes,
        n1 and n2, are connected by an edge.
            args:
                n1, n2: Vals association for node to be verified"""
        try:
            if n2 in self.g_dict[n1] or n1 in self.g_dict[n2]:
                return True
            else:
                return False
        except KeyError:
            return False
