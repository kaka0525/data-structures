from stack import Stack


def test_push_to_stack():
    new_stack_push = Stack()
    new_stack_push.push('box1')
    assert new_stack_push.ll is not None
    assert new_stack_push.ll.head.val is 'box1'
    new_stack_push.push('box2')
    new_stack_push.push('box3')
    assert new_stack_push.ll.head.val is 'box3'


def test_pop_from_stack():
    new_stack_pop = Stack()
    assert new_stack_pop.ll.head is None
    new_stack_pop.push('box1')
    new_stack_pop.push('box2')
    assert new_stack_pop.ll.head.val is 'box2'
    new_stack_pop.pop()
    assert new_stack_pop.ll.head.val is 'box1'
