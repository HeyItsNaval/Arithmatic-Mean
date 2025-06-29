from sympy import sympify


def is_definitely_real(value):
    try:
        expr = sympify(value)
        # Check if it's a real number and not an integer
        return expr.is_real is True
    except:
        return False