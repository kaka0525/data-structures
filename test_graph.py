from graph import Graph
import pytest
from string import ascii_uppercase
from random import randint


@pytest.fixture()
def populate():
    """
    Fixture will pre-populate random, range(x), nodes in Graph.
    In addition, it will also pre-populate random, range(y), edges for nodes
        that already exist.

    This will not generate duplicate nodes or edges, and will not allow node to
        create edges to iteself.
    """
    gph = Graph()
    for num in range(10):
        try:
            rand = ascii_uppercase[randint(0, 25)]
            gph.add_node(rand)
        except KeyError:
            continue

    nodes = gph.nodes()
    for num in range(2):
        for node in nodes:
            rand = nodes[randint(0, len(nodes) - 1)]
            try:
                gph.add_edge(node, rand)
            except KeyError:
                continue

    return gph


def test_return_nodes(populate):
    assert type(populate.nodes()) is list
    nodes = populate.nodes()
    assert type(nodes[0]) is str


def test_return_edges(populate):
    nodes = populate.nodes()
    node = nodes[0]
    edges = populate.neighbors(node)
    edge = edges[0]
    assert type(edge) is str


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
    edges = populate.neighbors(node)
    assert edge not in edges


def test_has_node(populate):
    nodes = populate.nodes()
    node = nodes[0]
    assert populate.has_node(node) is True
    assert populate.has_node('Beans') is False


def test_neighbors(populate):
    nodes = populate.nodes()
    node = nodes[0]
    edges = populate.neighbors(node)
    assert populate.g_dict[node] == edges


def test_depth_trav(populate):
    """This is weak. Having a hard time asserting on unknowns."""
    with pytest.raises(KeyError):
        populate.depth_trav('beans')
    nodes = populate.nodes()
    node = nodes[0]
    edges = populate.neighbors(node)
    trav = populate.depth_trav(node)
    if len(edges) > 0:
        assert edges[0 - len(edges)] in trav


def test_breadth_trav(populate):
    """This is weak. Having a hard time asserting on unknowns."""
    with pytest.raises(KeyError):
        populate.depth_trav('beans')
    nodes = populate.nodes()
    node = nodes[0]
    edges = populate.neighbors(node)
    trav = populate.depth_trav(node)
    if len(edges) > 0:
        assert edges[0 - len(edges)] in trav
