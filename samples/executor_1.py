#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
import threading
import time


def task(nb, name):
    print('Executing {}... ({})'.format(name, threading.current_thread()))
    result = 0
    for i in range(nb):
        result += i
        time.sleep(0.5)
        print('Result: {} {} ({})'.format(result, name, threading.current_thread()))
    print('Task executed {}'.format(threading.current_thread()))


def main():
    print('\n')
    executor = ThreadPoolExecutor(max_workers=3)
    executor.submit(task, 3, 'Task #1')
    executor.submit(task, 5, 'Task #2')
    executor.submit(task, 2, 'Task #3')


if __name__ == '__main__':
    main()
