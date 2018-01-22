#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Fibonacci numbers module
"""


def fib(n):
    """Print Fibonacci series up to n

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
    """

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


def main():
    """The entry point of the script

    """
    fib(10)
    print(fib2(20))


if __name__ == '__main__':
    main()
