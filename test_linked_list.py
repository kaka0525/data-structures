from linked_list import LinkList


def test_list_size():
    li = LinkList('List')
    li.insert('node1')
    li.insert('node2')
    li.insert('node3')
    assert li.size is not None
    assert li.size is 3


def test_list_search():
    pass


def test_list_display():
    li = LinkList('List')
    li.insert('node1')
    li.insert('node2')
    li.insert('node3')
    assert li.display() == ('node3', 'node2', 'node1')


def test_list_remove():
    li = LinkList('List')
    li.insert('node1')
    li.insert('node2')
    li.insert('node3')
    li.remove('node3')


def test_list_insert():
    li = LinkList('List')
    li.insert('node1')
    li.insert('node2')
    li.insert('node3')
    assert li.head is not None
    assert li.head.val is 'node3'


def test_list_pop():
    pass
