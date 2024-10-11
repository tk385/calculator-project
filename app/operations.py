# The operations module contains the four basic arithmetic functions: addition, subtraction, multiplication, and division.

def addition(x, y):
    """
    Returns the sum of two numbers.
    
    :param x: First number
    :param y: Second number
    :return: Sum of x and y
    """
    return x + y

def subtraction(x, y):
    """
    Returns the result of subtracting the second number from the first.
    
    :param x: First number
    :param y: Second number
    :return: Difference of x and y
    """
    return x - y

def multiplication(x, y):
    """
    Returns the product of two numbers.
    
    :param x: First number
    :param y: Second number
    :return: Product of x and y
    """
    return x * y

def division(x, y):
    """
    Returns the result of dividing the first number by the second.
    Raises an error if the second number is zero.
    
    :param x: First number
    :param y: Second number
    :raises ValueError: If y is zero
    :return: Quotient of x and y
    """
    if y == 0:
        raise ValueError("Division by zero is not allowed.")  # Handle division by zero by raising an exception
    return x / y
