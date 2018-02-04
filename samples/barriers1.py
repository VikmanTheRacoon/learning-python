#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random


class MyThread(threading.Thread):
    def __init__(self, barrier):
        super().__init__()
        self.barrier = barrier

    def run(self):
        print('Thread {} working on something...'.format(self.getName()))
        time.sleep(random.randint(1, 10))
        print('Thread {} waiting for others...'.format(self.getName()))
        self.barrier.wait()
        print('Barrier has been lifted: continuing')


def main():
    my_barrier = threading.Barrier(4)
    threads = []
    for i in range(4):
        t = MyThread(my_barrier)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
