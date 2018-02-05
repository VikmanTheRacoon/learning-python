#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import queue


def my_subscriber(my_queue):
    time.sleep(1)
    while not my_queue.empty():
        item = my_queue.get()
        if item is None:
            break
        print('{} Removed {} from queue'.format(threading.current_thread().getName(), item))
        my_queue.task_done()


def main():
    my_queue = queue.Queue()
    for i in range(5):
        print('Put {} in my_queue'.format(i))
        my_queue.put(i)
    print('my_queue populated')
    t = threading.Thread(target=my_subscriber, args=(my_queue,))
    t.start()
    my_queue.join()
    print('Queue is now empty')


if __name__ == '__main__':
    main()
