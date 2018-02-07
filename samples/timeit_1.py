#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import time


def func1():
    print("Function 1 Executing")
    time.sleep(5)
    print("Function 1 complete")


def func2():
    print("Function 2 executing")
    time.sleep(6)
    print("Function 2 complete")


def main():
    t1 = timeit.Timer("func1()", setup="from __main__ import func1")
    times = t1.repeat(repeat=2, number=1)
    for t in times:
        print("{} Seconds: ".format(t))
    t2 = timeit.Timer("func2()", setup="from __main__ import func2")
    times = t2.repeat(repeat=2, number=1)
    for t in times:
        print("{} Seconds: ".format(t))


if __name__ == '__main__':
    main()
