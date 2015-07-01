from binary_heap import MinBinaryHeap
import pytest


@pytest.fixture()
def heap():
    bh = MinBinaryHeap([1, 4, 16, 22, 28, 34, 56, 67, 69])
    return bh


def test_push_to_new_heap(heap):
    heap.push(18)
    assert heap[4] is 18
    heap.push(2)
    assert heap[1] is 2


def test_pop_from_heap(heap):
    heap.pop()
    assert heap[0] is 4
    assert heap[3] is 67


def test_pop_from_empty_heap():
    with pytest.raises(IndexError):
        heap.pop()


def test_push_iter_to_heap():
    bh = MinBinaryHeap([2, 24, 1, 48, 3, 50, 90, 67, 1000])
    assert bh[0] is 1
    assert bh[4] is # something


def test_push_non_iter_to_heap():
    with pytest.raises(TypeError):
        bh = MinBinaryHeap(['beans', 'bears', 'bottles'])
