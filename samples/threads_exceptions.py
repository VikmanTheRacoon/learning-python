#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import threading
import time
import queue


def my_worker(my_queue):
    while True:
        try:
            time.sleep(2)
            raise Exception("Exception Thrown In Child Thread {}".format(threading.current_thread()))
        except:
            my_queue.put(sys.exc_info())
            break


def main():
    my_queue = queue.Queue()
    my_thread = threading.Thread(target=my_worker, args=(my_queue,))
    my_thread.start()
    while True:
        try:
            exception = my_queue.get()
        except queue.Empty:
            pass
        else:
            print('-->', exception)
            break


if __name__ == '__main__':
    main()
