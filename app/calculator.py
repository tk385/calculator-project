from app.operations import addition, subtraction, multiplication, division

def calculator():
    """
    This function is a simple REPL (Read-Eval-Print Loop) calculator.
    It allows users to input an operation (add, subtract, multiply, divide) and two numbers.
    The program continues to run until the user types 'exit'.
    """
    print("Welcome to the calculator!")  # Greets the user when the calculator starts
    
    while True:
        # Prompt the user for input and split the input into an operation and two numbers
        user_input = input("Enter operation and two numbers (e.g., add 2 3) or type 'exit': ").split()
        
        # If the user enters 'exit', stop the calculator loop
        if user_input[0] == "exit":
            break
        
        # Extract the operation and two numbers from the user input
        operation, x, y = user_input[0], float(user_input[1]), float(user_input[2])
        
        # Check which operation the user entered and call the corresponding function
        if operation == "add":
            print(f"Result: {addition(x, y)}")  # Call the addition function
        elif operation == "subtract":
            print(f"Result: {subtraction(x, y)}")  # Call the subtraction function
        elif operation == "multiply":
            print(f"Result: {multiplication(x, y)}")  # Call the multiplication function
        elif operation == "divide":
            # Call the division function and handle division by zero errors
            try:
                print(f"Result: {division(x, y)}")
            except ValueError as e:
                print(e)  # Print the error message for division by zero
        else:
            # If the operation is not recognized, notify the user
            print("Unknown operation")
