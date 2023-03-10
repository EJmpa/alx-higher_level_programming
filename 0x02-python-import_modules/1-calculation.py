#!/usr/bin/python3
# 1-calculation.py

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    import calculator_1

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
