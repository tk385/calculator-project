import pytest
from app.calculator import calculator
from io import StringIO
import sys

# Helper function that allows us to simulate user input and capture printed output
def simulate_calculator_input(monkeypatch, inputs):
    """
    Simulates user input and captures output for the calculator REPL.
    
    :param monkeypatch: pytest fixture to mock input
    :param inputs: List of strings to simulate user input
    :return: Captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture the output printed by the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__  # Reset standard output after capturing
    return captured_output.getvalue()


# Test for the addition operation in the calculator REPL
def test_calculator_add(monkeypatch):
    """
    Test the addition operation in the calculator REPL.
    """
    inputs = ["add 2 3", "exit"]  # Simulate user input: add 2 and 3, then exit
    output = simulate_calculator_input(monkeypatch, inputs)
    assert "Result: 5.0" in output  # Check if the output contains the correct result


# Test for the subtraction operation in the calculator REPL
def test_calculator_subtract(monkeypatch):
    """
    Test the subtraction operation in the calculator REPL.
    """
    inputs = ["subtract 5 3", "exit"]  # Simulate user input: subtract 5 and 3, then exit
    output = simulate_calculator_input(monkeypatch, inputs)
    assert "Result: 2.0" in output  # Check if the output contains the correct result


# Test for the multiplication operation in the calculator REPL
def test_calculator_multiply(monkeypatch):
    """
    Test the multiplication operation in the calculator REPL.
    """
    inputs = ["multiply 4 5", "exit"]  # Simulate user input: multiply 4 and 5, then exit
    output = simulate_calculator_input(monkeypatch, inputs)
    assert "Result: 20.0" in output  # Check if the output contains the correct result


# Test for the division operation in the calculator REPL
def test_calculator_divide(monkeypatch):
    """
    Test the division operation in the calculator REPL.
    """
    inputs = ["divide 10 2", "exit"]  # Simulate user input: divide 10 by 2, then exit
    output = simulate_calculator_input(monkeypatch, inputs)
    assert "Result: 5.0" in output  # Check if the output contains the correct result


# Test for division by zero in the calculator REPL
def test_calculator_divide_by_zero(monkeypatch):
    """
    Test the division by zero operation in the calculator REPL.
    """
    inputs = ["divide 10 0", "exit"]  # Simulate user input: divide 10 by 0, then exit
    output = simulate_calculator_input(monkeypatch, inputs)
    assert "Division by zero is not allowed" in output  # Check for the error message
