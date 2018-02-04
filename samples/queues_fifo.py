#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import queue


def my_subscriber(my_queue):
    while not my_queue.empty():
        item = my_queue.get()
        if item is None:
            break
        print('{} Removed {} from queue'.format(threading.current_thread().getName(), item))
        my_queue.task_done()
        time.sleep(1)


def main():
    my_queue = queue.Queue()
    for i in range(10):
        my_queue.put(i)
    print('my_queue populated')
    threads = []
    for i in range(4):
        t = threading.Thread(target=my_subscriber, args=(my_queue,))
        t.start()
        threads.append(t)
    my_queue.join()
    print('Queue is empty')
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
