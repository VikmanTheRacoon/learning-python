#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


def main():
    double_ended_queue = collections.deque('123456')
    print("Deque: {}".format(double_ended_queue))
    double_ended_queue.rotate(3)
    print("Deque: {}".format(double_ended_queue))
    double_ended_queue.rotate(-2)
    print("Deque {}".format(double_ended_queue))


if __name__ == '__main__':
    main()
