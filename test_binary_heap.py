from binary_heap import MinBinaryHeap
import pytest


@pytest.fixture()
def heap():
    bh = MinBinaryHeap([1, 4, 16, 22, 28, 34, 56, 67, 69])
    return bh


def test_push_to_new_heap(heap):
    heap.push(18)
    assert heap.heap_list[4] is 18
    heap.push(2)
    assert heap.heap_list[1] is 2
    assert heap.heap_list[-1] is 18


def test_pop_from_heap(heap):
    heap.pop()
    assert heap.heap_list[0] is 4
    assert heap.heap_list[3] is 67


def test_pop_from_empty_heap():
    with pytest.raises(IndexError):
        MinBinaryHeap().pop()


def test_push_iter_to_heap():
    bh = MinBinaryHeap([2, 24, 1, 48, 3, 50, 90, 67, 1000])
    assert bh.heap_list[0] is 1
    assert bh.heap_list[4] is 24


def test_push_non_iter_to_heap():
    with pytest.raises(TypeError):
        MinBinaryHeap(['beans', 'bears', 'bottles'])


def test_edge_case():
    h = MinBinaryHeap([1, 5, 8, 7, 9, 10, 11])
    h.push(4)
    assert h.heap_list == [1, 4, 8, 5, 9, 10, 11, 7]


def test_duplicate():
    h = MinBinaryHeap([1, 2, 3])
    h.push(1)
    assert h.heap_list == [1, 1, 3, 2]
