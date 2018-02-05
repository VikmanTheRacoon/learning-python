#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import queue


def my_subscriber(my_queue):
    time.sleep(1)
    while not my_queue.full():
        my_queue.put(1)
        print('{} Appended 1 to queue'.format(threading.current_thread().getName()))
        time.sleep(1)


def main():
    my_queue = queue.Queue(maxsize=5)

    threads = []
    for i in range(4):
        t = threading.Thread(target=my_subscriber, args=(my_queue,))
        t.start()
        threads.append(t)
    my_queue.join()
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
