#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random


def worker_a():
    print("Thead {} started".format(threading.current_thread().getName()))
    time.sleep(random.randint(1, 2))
    print("Thead {} finished".format(threading.current_thread().getName()))


def worker_b():
    print("Thead {} started".format(threading.current_thread().getName()))
    time.sleep(random.randint(1, 2))
    print("Thead {} finished".format(threading.current_thread().getName()))


def main():
    threads = []
    for i in range(2):
        thread = threading.Thread(target=worker_a, name='Worker_A-' + str(i))
        thread.start()
        threads.append(thread)
    for i in range(2):
        thread = threading.Thread(target=worker_b, name='Worker_B-' + str(i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
