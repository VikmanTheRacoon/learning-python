#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def my_thread(my_event):
    while not my_event.isSet():
        print('Waiting for my_event to be set...')
        time.sleep(1)
    print('Stopping: my_event has been set!')


def main():
    my_event = threading.Event()
    thread1 = threading.Thread(target=my_thread, args=(my_event,))
    thread1.start()
    time.sleep(10)
    my_event.set()


if __name__ == '__main__':
    main()
