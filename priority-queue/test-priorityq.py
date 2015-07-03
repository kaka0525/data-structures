from priorityq import PriorityQ
import pytest
from random import randint


@pytest.fixture()
def pq_setup():
    """Create random order entry of values into priority queue"""
    pq = PriorityQ()

    for num in range(1, 200):
        pq.insert(randint(1, 10))
    return pq


def test_check_heap_priority(pq_setup):
    p1 = pq_setup.priorities[1]
    assert p1.heap_list[0] < p1.heap_list[2]
    assert p1.heap_list[3] < p1.heap_list[6]


def test_pq_insert(pq_setup):
    p6 = pq_setup.priorities[6]
    p6_len = len(p6.heap_list)
    pq_setup.insert(6)
    assert len(p6.heap_list) == p6_len + 1


def test_pq_pop_with_arg(pq_setup):
    with pytest.raises(TypeError):
        pq_setup.pop(2)
    with pytest.raises(TypeError):
        pq_setup.pop('a')


def test_pq_peek(pq_setup):
    p1 = pq_setup.priorities[1]
    pre_pop = p1.heap_list[0]
    post_pop = pq_setup.pop()
    assert pre_pop == post_pop


def test_pq_create():
    pq = PriorityQ()
    assert pq.priorities == {}


@pytest.fixture()
def pq_setup_large():
    pq = PriorityQ()

    for num in range(1, 10001):
        pq.insert(randint(1, 10))
    return pq


def test_insert_lrg_check_heap(pq_setup_large):
    pq4 = pq_setup_large.priorities[4]
    assert pq4.heap_list[20] < pq4.heap_list[42]


def test_pq_insert_len():
    pq = PriorityQ()
    for num in range(10):
        pq.insert(1)
    p1 = pq.priorities[1]
    assert len(p1.heap_list) is 10
    pq.insert(1)
    assert len(p1.heap_list) is 11
