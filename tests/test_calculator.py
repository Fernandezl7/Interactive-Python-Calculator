'''My Calculator Test'''
from apps.calculator import Calculator

def test_addition():
    '''Testing addition function'''
    assert Calculator.add(2,2) == 4
def test_subtraction():
    '''Testing subtraction function'''
    assert Calculator.subtract(2,2) == 0
def test_divide():
    '''Testing divide function'''
    assert Calculator.divide(2,2) == 1
def test_multiply():
    '''Tetsing multiplication function'''
    assert Calculator.multiply(2,2) == 2