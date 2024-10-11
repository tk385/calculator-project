import pytest
from app.operations import addition, subtraction, multiplication, division

# Test cases for the addition function
def test_addition():
    """
    Test cases for the addition function with positive and negative numbers.
    """
    assert addition(4, 5) == 9  # Test a simple addition
    assert addition(-1, 1) == 0  # Test addition with negative and positive values

# Test cases for the subtraction function
def test_subtraction():
    """
    Test cases for the subtraction function with positive and negative numbers.
    """
    assert subtraction(10, 5) == 5  # Test a simple subtraction
    assert subtraction(-1, 1) == -2  # Test subtraction with negative and positive values

# Test cases for the multiplication function
def test_multiplication():
    """
    Test cases for the multiplication function with positive and negative numbers.
    """
    assert multiplication(3, 5) == 15  # Test a simple multiplication
    assert multiplication(-1, 1) == -1  # Test multiplication with negative and positive values

# Test cases for the division function
def test_division():
    """
    Test cases for the division function, including division by zero.
    """
    assert division(10, 2) == 5  # Test a simple division
    with pytest.raises(ValueError):
        division(10, 0)  # Test that division by zero raises a ValueError
