def generator_square_polynom(a, b, c):
    def calculate_square_polynom_value(x):
        return a * x**2 + b*x + c

    return calculate_square_polynom_value
