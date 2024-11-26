from math import sqrt, pi

__doc__ = 'This package is able to calculate 10th, 11th, and 12th maths equations..'
__package__ = 'Maths'


def quadratic(a, b, c):
    x = (-b) + sqrt((b * b) - 4 * (a * c))
    x = x / (2 * a)
    y = (-b) - sqrt((b * b) - 4 * (a * c))
    y = y / (2 * a)
    return x, y


def power(a, b, n):
    # __doc__ = 'This Function is able to calculate any power of two numbers '
    i = 0
    x = 1
    for i in range(n):
        x *= (a + b)
    return x


if __name__ == "__main__":
    z = power(2, 2, 6)
    print(z)
    # Calling this function and checking..
    z = quadratic(1, 5, 4)
    print(z)
