import pytest
from stack import Stack


def test_push_to_stack():
    new_stack_push = Stack()
    assert new_stack_push.top is None
    new_stack_push.push('box1')
    assert new_stack_push.top is not None
    assert new_stack_push.top.val is 'box1'
    new_stack_push.push('box2')
    new_stack_push.push('box3')
    assert new_stack_push.top.val is 'box3'


def test_pop_from_stack():
    new_stack_pop = Stack()
    assert new_stack_pop.top is None
    new_stack_pop.push('box1')
    new_stack_pop.push('box2')
    assert new_stack_pop.top.val is 'box2'
    new_stack_pop.pop()
    assert new_stack_pop.top.val is 'box1'
    with pytest.raises(TypeError):
        pass  # Need to verify error
