def safe_divide(numerator, denominator):
    try:
        result = int(numerator)/int(denominator)
    except ZeroDivisionError:
        return "Cannot be divided by zero"
    except ValueError:
        return "Must be numerical number"
    return result