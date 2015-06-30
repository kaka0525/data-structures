import pytest
from proper_parenthetics import proper_parenthetics


def test_proper_parenthetics():
    assert proper_parenthetics('()') == 0
    assert proper_parenthetics('') == 0
    assert proper_parenthetics(')(') == -1
    assert proper_parenthetics('())') == -1
    assert proper_parenthetics('(') == 1
    assert proper_parenthetics(')') == -1
    assert proper_parenthetics('))))))((((((') == -1
    assert proper_parenthetics('()(') == 1
    assert proper_parenthetics('()()()()()()()(') == 1
    assert proper_parenthetics('()()()()()()())') == -1
    assert proper_parenthetics('(((((((((())))))))))') == 0
