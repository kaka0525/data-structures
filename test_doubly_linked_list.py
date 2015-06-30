from doubly_linked_list import Doublylinkedlist
import pytest


@pytest.fixture()
def list_setup():
    dbl_list = Doublylinkedlist()
    dbl_list.insert(1)
    dbl_list.insert(2)
    dbl_list.insert(3)
    dbl_list.insert(4)
    return dbl_list


def test_empty_list():
    dbl_list = Doublylinkedlist()
    assert dbl_list.head is None
    assert dbl_list.tail is None


def test_insert_node_at_head(list_setup):
    assert list_setup.head.val is 4
    list_setup.insert(5)
    assert list_setup.head.val is 5


def test_append_node_at_tail(list_setup):
    assert list_setup.tail.val is 1
    list_setup.append(5)
    list_setup.append(6)
    assert list_setup.tail.val is 6


def test_pop_node_at_head(list_setup):
    assert list_setup.pop() == 4
    list_setup.insert(5)
    assert list_setup.pop() == 5


def test_shift_node_at_tail(list_setup):
    list_setup.shift()
    assert list_setup.tail.val is 2
    list_setup.shift()
    assert list_setup.tail.val is 3


def test_remove_node_from_list(list_setup):
    pass


def test_remove_no_argument(list_setup):
    with pytest.raises(ValueError):
        list_setup.remove()
    assert ValueError
