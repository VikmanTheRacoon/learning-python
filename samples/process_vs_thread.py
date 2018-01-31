#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
from multiprocessing import Process
import time


def worker():
    time.sleep(0.5)


def main():
    t0 = time.time()
    threads = []
    i = 50
    for i in range(i):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)
    t1 = time.time()
    print('\n\nTotal for creating {} threads: {}'.format(i + 1, t1 - t0))
    for thread in threads:
        thread.join()

    t0 = time.time()
    procs = []
    i = 50
    for i in range(i):
        proc = Process(target=worker)
        proc.start()
        procs.append(proc)
    t1 = time.time()
    print('Total for creating {} processes: {}'.format(i + 1, t1 - t0))
    for proc in procs:
        proc.join()


if __name__ == '__main__':
    main()
