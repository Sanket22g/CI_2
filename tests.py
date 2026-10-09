import pytest 

def square(n):
    return n * n 

def test_square_positive():
    assert square(2) == 4

def test_square_negative():
    assert square(-2) == 4

def test_square_zero():
    assert square(0) == 0

def testInvalidInput():
    with pytest.raises(TypeError):
        square("a")

def testLargeInput():
    assert square(1000000) == 1000000000000

def testFloatInput():
    assert square(2.5) == 6.25