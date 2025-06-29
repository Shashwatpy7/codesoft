import numpy as np

def calculator(num1, num2, operation):
    result = None

    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = "Division by zero not allowed" if num2 == 0 else num1 / num2
        elif operation == '//':
            result = "Division by zero not allowed" if num2 == 0 else num1 // num2
        elif operation == '^':
            result = num1 ** num2
        elif operation == 'sqrt':
            result = np.sqrt(num1)
        elif operation == 'sin':
            result = np.sin(np.radians(num1))
        elif operation == 'cos':
            result = np.cos(np.radians(num1))
        elif operation == 'tan':
            result = np.tan(np.radians(num1))
        elif operation == 'log':
            result = np.log(num1)
        elif operation == 'exp':
            result = np.exp(num1)
        else:
            result = 'Invalid Operator'

    except Exception as e:
        result = f"Error occurred: {e}"

    return result
