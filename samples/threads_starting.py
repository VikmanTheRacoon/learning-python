#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random


def execute_thread(i):
    print("Thread {} started".format(i))
    sleepTime = random.randint(1, 10)
    time.sleep(sleepTime)
    print("Thread {} finished executing".format(i))


def main():
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        thread.start()
    for t in threading.enumerate():
        print("Active Thread:", t)


if __name__ == '__main__':
    main()
