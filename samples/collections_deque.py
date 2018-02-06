#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


def main():
    double_ended_queue = collections.deque('0123456789')
    print('Deque: {}'.format(double_ended_queue))
    for item in double_ended_queue:
        print('Item {}'.format(item))
    print("Left Most Element: {}".format(double_ended_queue[0]))
    print("Right Most Element: {}".format(double_ended_queue[-1]))


if __name__ == '__main__':
    main()
