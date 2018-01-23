#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Fibonacci series module
"""


def fib(n):
    """Prints Fibonacci series up to n

    Args:
        n: High limit of the serie

    Returns:
    """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    """Calculates Fibonacci series up to n

    Args:
        n: High limit of the serie

    Returns:
        A list of the elements of the serie
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


if __name__ == '__main__':
    import sys

    fib(int(sys.argv[1]))
