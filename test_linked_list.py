import pytest
from linked_list import LinkList


def test_list_size():
    one_node = LinkList()
    one_node.insert('node1')
    many_nodes = LinkList()
    many_nodes.insert('node1')
    many_nodes.insert('node2')
    many_nodes.insert('node3')
    many_nodes.insert('node4')
    many_nodes.insert('node5')
    empty = LinkList()
    assert empty.size_ is 0
    assert one_node.size_ is 1
    assert many_nodes.size_ is 5
    many_nodes.remove('node3')
    assert many_nodes.size_ is 4


def test_list_search():
    many_nodes = LinkList()
    many_nodes.insert('node1')
    many_nodes.insert('node2')
    many_nodes.insert('node3')
    many_nodes.insert('node4')
    many_nodes.insert('node5')
    many_nodes.insert('node6')
    many_nodes.pop()
    assert many_nodes.search('node5') is many_nodes.head
    assert (many_nodes.search('node3') is
            many_nodes.head.pointer.pointer)
    with pytest.raises(ValueError):
        many_nodes.search('node6')
    with pytest.raises(ValueError):
        many_nodes.search('node7')


def test_list_display():
    li = LinkList()
    li.insert('node1')
    li.insert('node2')
    li.insert('node3')
    many_nodes = LinkList()
    many_nodes.insert('node1')
    many_nodes.insert('node2')
    many_nodes.insert('node3')
    many_nodes.insert('node4')
    many_nodes.insert('node5')
    many_nodes.insert('node6')
    many_nodes.pop()
    empty = LinkList()
    assert li.display() == "('node3','node2','node1')"
    assert many_nodes.display() == "('node5','node4','node3','node2','node1')"
    assert empty.display() == li


def test_list_remove():
    li = LinkList()
    li.insert('node1')
    li.insert('node2')
    li.insert('node3')
    li.remove('node3')
    many_nodes = LinkList()
    many_nodes.insert('node1')
    many_nodes.insert('node2')
    many_nodes.insert('node3')
    many_nodes.insert('node4')
    many_nodes.insert('node5')
    many_nodes.insert('node6')
    many_nodes.remove('node4')
    one_node = LinkList()
    one_node.insert('node1')
    one_node.remove('node1')
    assert li.size_ is 2
    assert li.display() == ('node2', 'node1')
    assert many_nodes.size_ is 5
    assert many_nodes.display() == ('node6', 'node5', 'node3',
                                    'node2', 'node1')
    assert one_node.size_ is 0


def test_list_insert():
    li = LinkList()
    li.insert('node1')
    li.insert('node2')
    li.insert('node3')
    li.insert('node3')
    li.insert('node4')
    assert li.size_ is 5
    assert li.head.val is 'node4'
    assert li.head.pointer.val is 'node3'


def test_list_pop():
    many_nodes = LinkList()
    many_nodes.insert('node1')
    many_nodes.insert('node2')
    many_nodes.insert('node3')
    many_nodes.insert('node4')
    many_nodes.insert('node5')
    many_nodes.insert('node6')
    many_nodes.pop()
    one_node = LinkList()
    one_node.insert('node1')
    one_node.pop()
    empty_node = LinkList()
    assert many_nodes.size_ is 5
    assert one_node.size_ is 0
    with pytest.raises(ValueError):
        empty_node.pop()
