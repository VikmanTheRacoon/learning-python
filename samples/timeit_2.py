#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import random
import time


def time_this(func):
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        run_time = timeit.default_timer() - start_time
        print('Function {} took {} seconds to execute'.format(func.__name__, run_time))
        return value

    return function_timer


@time_this
def long_runner():
    for x in range(5):
        sleep_time = random.choice(range(1, 3))
        time.sleep(sleep_time)


def main():
    long_runner()


if __name__ == '__main__':
    main()
