def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
    except:
        return "Error: Please enter numeric values only."
    try:
        result = num/den
        return f"The result of the division is {result}"
    except:
        return "Error: Cannot divide by zero."