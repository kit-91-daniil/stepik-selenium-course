import pytest

def test_abs1():
    assert abs(-42) == 42, "Something is wrong in test_abs1"


def test_abs2():
    assert abs(-42) == -42, "Something is wrong in test_abs2"


def test_exception_expectation():
    with pytest.raises(TypeError):
        raise ZeroDivisionError
        # raise TypeError

