#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random

counter = 1
lock = threading.Lock()


def worker_a():
    global counter
    lock.acquire()
    try:
        while counter < 10:
            counter += 1
            print("Worker A is incrementing counter to {}".format(counter))
            sleep_time = random.randint(0, 1)
            time.sleep(sleep_time * .5)
    finally:
        lock.release()


def worker_b():
    global counter
    lock.acquire()
    try:
        while counter > -10:
            counter -= 1
            print("Worker B is decrementing counter to {}".format(counter))
            sleep_time = random.randint(0, 1)
            time.sleep(sleep_time * .5)
    finally:
        lock.release()


def main():
    t0 = time.time()
    thread1 = threading.Thread(target=worker_a)
    thread2 = threading.Thread(target=worker_b)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    print("Execution time {}".format(t1 - t0))


if __name__ == '__main__':
    main()
