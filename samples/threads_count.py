#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import random
import time


def worker(i):
    time.sleep(random.randint(2, 10))


def main():
    for i in range(5000):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
    count = threading.active_count()
    while count > 1:
        count = threading.active_count()
        print("{} active threads".format(count))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
