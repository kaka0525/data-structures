from parens import paren_check
import pytest


@pytest.fixture()
def opened():
    return "(("


@pytest.fixture()
def closed():
    return "()"


@pytest.fixture()
def not_opened():
    return ")"


@pytest.fixture()
def no_parens():
    return "l;akjsdfoij"


def test_open_close_correct(closed):
    assert paren_check(closed) is 0
    assert paren_check(closed) is not 1 or -1


def test_close_paren_first(not_opened):
    assert paren_check(not_opened) is -1
    assert paren_check(not_opened) is not 0 or -1


def test_open_no_close(opened):
    assert paren_check(opened) is 1
    assert paren_check(opened) is not -1 or 0


def test_no_parens_in_str(no_parens):
    assert paren_check(no_parens) is 0
    assert paren_check(no_parens) is not -1 or 1
