#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    """Lists as piles
    """

    # Create a stack
    my_stack = [1, 2, 3, 4]
    print("my_stack", my_stack)

    # Push values on the stack
    my_stack.append(5)
    my_stack.append(6)
    my_stack.append(7)
    print("my_stack", my_stack)

    # Pop values from the stack
    print("Poped value", my_stack.pop())
    print("my_stack", my_stack)
    print("Poped value", my_stack.pop())
    print("my_stack", my_stack)
    print("Poped value", my_stack.pop())
    print("my_stack", my_stack)
    print("Poped value", my_stack.pop())
    print("my_stack", my_stack)


if __name__ == '__main__':
    main()
