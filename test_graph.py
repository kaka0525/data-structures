from graph import Graph
import pytest
from string import ascii_uppercase
from random import randint


@pytest.fixture()
def populate():
    """Need to refactor this for more random inserts"""
    gph = Graph()
    for num in range(15):
        rand = ascii_uppercase[randint(0, 25)]
        gph.add_node(rand)

    nodes = gph.nodes()
    for num in range(5):
        for node in nodes:
            rand = nodes[randint(0, len(nodes) - 1)]
            gph.add_edge(node, rand)

    return gph


def test_return_nodes(populate):
    assert type(populate.nodes()) is list
    nodes = populate.nodes()
    assert nodes[0] is str


def test_return_edges(populate):
    assert type(populate.edges()) is tuple


def test_add_new_node(populate):
    populate.add_node('E')
    assert populate['E'] in populate.nodes()
    assert populate['E'] == []


def test_add_new_edge(populate):
    populate.add_edge('A', 'C')
    assert 'C' in populate['A']


def test_delete_node(populate):
    nodes = populate.nodes()
    node = nodes[0]
    populate.del_node(node)
    assert node not in populate


def test_delete_edge(populate):
    nodes = populate.nodes()
    


def test_has_node(populate):
    assert populate.has_node('A') is True
    assert populate.has_node('Ball') is False


def test_neighbors(populate):
    assert populate.neighbors('C') == []
    """Need to finish this"""


def test_adjacent(populate):
    pass


def test_empty_graph():
    pass
