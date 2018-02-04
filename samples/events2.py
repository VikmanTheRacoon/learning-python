#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def my_thread_1(my_event_1):
    my_event_2 = threading.Event()
    threads_2 = []
    print('Starting sub-threads...')
    for i in range(4):
        t = threading.Thread(target=my_thread_2, args=(my_event_2,))
        t.start()
        threads_2.append(t)
    time.sleep(2)
    print('Waiting for my_event_1 to be set...')
    while not my_event_1.isSet():
        time.sleep(2)
    print('Stopping: my_event_1 has been set!')
    my_event_2.set()
    for t in threads_2:
        t.join()


def my_thread_2(my_event_2):
    print('Waiting for my_event_2 to be set...')
    while not my_event_2.isSet():
        time.sleep(2)
    print('Stopping: my_event_2 has been set!')


def main():
    my_event_1 = threading.Event()
    threads_1 = []
    print('Starting threads...')
    for i in range(4):
        t = threading.Thread(target=my_thread_1, args=(my_event_1,))
        t.start()
        threads_1.append(t)
    time.sleep(2)
    my_event_1.set()
    for t in threads_1:
        t.join()
    print('All threads stopped.')


if __name__ == '__main__':
    main()
