import pytest
from proper_parenthetics import proper_parenthetics


def test_balanced_parenthetics():
    assert proper_parenthetics('()') == 0
    assert proper_parenthetics('(((((((((())))))))))') == 0


def test_empty_parenthetics():
    assert proper_parenthetics('') == 0
    assert proper_parenthetics('         ') == 0


def test_broken_parenthetics():
    assert proper_parenthetics('))))))((((((') == -1
    assert proper_parenthetics('()()()()()()())') == -1


def test_open_parenthetics():
    assert proper_parenthetics('((((((((()))))))))(') == 1
    assert proper_parenthetics('((((((((()))))))))((((')


def test_odd_input():
    assert proper_parenthetics('(hello((((((world)))))))') == 0
    assert proper_parenthetics(')!(((!!!!!!!)))!)') == -1
    assert proper_parenthetics('(#((((((#()))#))))#)((') == 1
