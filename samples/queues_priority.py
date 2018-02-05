#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random
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
    my_queue = queue.PriorityQueue()
    for i in range(5):
        priority = random.randint(1, 10)
        print('Put {} in my_queue with priority {}'.format(i, priority))
        my_queue.put((priority, i))
    print('my_queue populated')
    threads = []
    for i in range(2):
        t = threading.Thread(target=my_subscriber, args=(my_queue,))
        t.start()
        threads.append(t)
    my_queue.join()
    print('Queue is empty')
    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
