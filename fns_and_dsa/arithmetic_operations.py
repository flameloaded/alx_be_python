def perform_operation(num1, num2, operation):
    if operation == "multiply":
        result = num1 * num2
    elif operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "divide":
        result = num1 / num2

    return result
    