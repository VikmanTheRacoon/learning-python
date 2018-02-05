#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


def main():
    double_ended_queue = collections.deque('1234567890')
    print('Deque: {}'.format(double_ended_queue))
    for item in double_ended_queue:
        print('Item {}'.format(item))

if __name__ == '__main__':
    main()
