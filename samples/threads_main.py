#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def worker():
    print("Child thread starting")
    time.sleep(1)
    print("Current thread: {}".format(threading.current_thread()))
    print("Main thread: {}".format(threading.main_thread()))


def main():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
