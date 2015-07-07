from graph import Graph
import pytest
from string import ascii_uppercase
from random import randint


@pytest.fixture()
def populate():
    gph = Graph()
    for num in range(15):
        try:
            rand = ascii_uppercase[randint(0, 25)]
            gph.add_node(rand)
        except KeyError:
            continue

    nodes = gph.nodes()
    for num in range(5):
        for node in nodes:
            rand = nodes[randint(0, len(nodes) - 1)]
            gph.add_edge(node, rand)

    return gph


def test_return_nodes(populate):
    assert type(populate.nodes()) is list
    nodes = populate.nodes()
    assert type(nodes[0]) is str


def test_return_edges(populate):
    # nodes = populate.nodes()
    # node = nodes[0]
    # edges = populate.edges()
    # assert type(edge) is str
    pass


def test_add_new_node(populate):
    try:
        populate.add_node('E')
        assert 'E' in populate.nodes()
        assert populate['E'] == []
    except KeyError:
        pass


def test_add_new_edge(populate):
    populate.add_edge('A', 'C')
    assert 'C' in populate['A']


def test_delete_node(populate):
    nodes = populate.nodes()
    node = nodes[0]
    populate.del_node(node)
    assert node not in populate.nodes()


def test_delete_edge(populate):
    nodes = populate.nodes()
    node = nodes[0]
    edges = populate.neighbors(node)
    edge = edges[0]
    populate.del_edge(node, edge)
    assert edge not in populate.edges(node)


def test_has_node(populate):
    pass


def test_neighbors(populate):
    pass


def test_adjacent(populate):
    pass


def test_empty_graph():
    pass
