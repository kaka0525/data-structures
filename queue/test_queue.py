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
    assert que.size_ is 0
    assert que.head is None
    assert que.prev is None


def test_add_many(queue):
    assert queue.size_ is 2
    assert queue.head is # finish
    assert queue.prev is # finish
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.head is # finish
    assert queue.prev is # finish


def test_dequeue(queue):
    assert queue.size_ is 2
    queue.dequeue()
    assert queue.size_ is 1
    queue.dequeue()
    assert queue.size_ is 0


def test_dequeue_empty(queue):
    assert queue.size_ is 2
    queue.dequeue()
    queue.dequeue()
    with pytest.raises(Exception):
        queue.dequeue()


def test_size(queue):
    assert queue.size_ is 2
    assert queue.size_ is not 1 or 3
    assert type(queue.size_) is int
    queue.dequeue()
    queue.dequeue()
    assert queue.size_ is 0
