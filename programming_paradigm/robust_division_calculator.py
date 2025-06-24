def safe_divide(numerator, denominator):
    try:
        result = int(numerator)/int(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Please enter numeric values only."
    return result