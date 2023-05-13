import pytest


def test_addition():
    result = 2 + 2
    assert result == 4


def test_run():
    result = [1, 2, 3, 4]
    assert 1 in result
