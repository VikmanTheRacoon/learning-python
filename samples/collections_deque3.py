#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


def main():
    double_ended_queue = collections.deque('123456')
    print('Deque: {}'.format(double_ended_queue))
    right_pop = double_ended_queue.pop()
    print('Right pop: {}'.format(right_pop))
    left_pop = double_ended_queue.popleft()
    print('Left pop: {}'.format(left_pop))
    print('Deque: {}'.format(double_ended_queue))


if __name__ == '__main__':
    main()
