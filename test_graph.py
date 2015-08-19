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
    for num in range(20):
        try:
            rand = ascii_uppercase[randint(0, 25)]
            gph.add_node(rand)
        except KeyError:
            continue

    nodes = gph.nodes()
    for num in range(3):
        for node in nodes:
            rand = nodes[randint(0, len(nodes) - 1)]
            weight = randint(-100, 101)
            try:
                gph.add_edge(node, rand, weight)
            except KeyError:
                continue

    return gph


@pytest.fixture()
def graph():
    gph = Graph()
    gph.add_node('A')
    gph.add_node('B')
    gph.add_node('C')
    gph.add_node('D')
    gph.add_node('E')
    gph.add_edge('A', 'B', 10)
    gph.add_edge('A', 'C', 5)
    gph.add_edge('B', 'C', 20)
    gph.add_edge('D', 'B', 5)

    return gph


def test_return_nodes(populate):
    assert type(populate.nodes()) is list
    nodes = populate.nodes()
    assert type(nodes[0]) is str


def test_return_edges(populate):
    nodes = populate.nodes()
    node = nodes[0]
    edges = populate.neighbors(node)
    edge = edges.iterkeys().next()
    assert type(edge) is str


def test_add_new_node(populate):
    try:
        populate.add_node('E')
        assert 'E' in populate.nodes()
        assert populate['E'] == {}
    except KeyError:
        pass


def test_add_new_edge(populate):
    populate.add_edge('A', 'C', 10)
    assert 'C' in populate['A']
    assert populate['A']['C'] == 10


def test_delete_node(populate):
    nodes = populate.nodes()
    node = nodes[0]
    populate.del_node(node)
    assert node not in populate.nodes()


def test_delete_edge(populate):
    nodes = populate.nodes()
    node = nodes[0]
    edges = populate.neighbors(node)
    edge = edges.iterkeys().next()
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


def test_depth_trav(graph):
    """This is weak. Having a hard time asserting on unknowns."""
    with pytest.raises(KeyError):
        graph.depth_trav('beans')
    node = 'A'
    trav = graph.depth_trav(node)
    assert node in trav
    assert 'D' not in trav


def test_breadth_trav(graph):
    """This is weak. Having a hard time asserting on unknowns."""
    with pytest.raises(KeyError):
        graph.depth_trav('beans')
    node = 'A'
    trav = graph.depth_trav(node)
    assert node in trav
    assert 'D' not in trav
