from queue import Queue
import pytest


@pytest.fixture()
def queue():
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    return que


def test_empty_queue():
    que = Queue()
    assert que._size is 0
    assert que.back is None


def test_add_many(queue):
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.back.val is 4


def test_dequeue(queue):
    queue.dequeue()
    assert queue._size is 1
    with pytest.raises(IndexError):
        queue.dequeue()
    assert queue._size is 0


def test_dequeue_empty(queue):
    assert queue._size is 2
    queue.dequeue()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_size(queue):
    assert type(queue._size) is int
    queue.dequeue()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert queue._size is 0
