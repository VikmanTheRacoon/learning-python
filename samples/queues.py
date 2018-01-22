#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def main():
    """Queues
    """

    # Create a queue
    my_queue = deque([1, 2, 3])
    print(my_queue)

    # Append element to the right
    my_queue.append(10)
    print(my_queue)

    # Append element to the left
    my_queue.appendleft(100)
    print(my_queue)

    # Pop from the right
    print("Deque", my_queue.pop())
    print(my_queue)

    # Pop from the left
    print("Deque", my_queue.popleft())
    print(my_queue)


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()
