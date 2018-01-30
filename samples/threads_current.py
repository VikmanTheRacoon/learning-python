#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading


def worker():
    print("Current thread is {}".format(threading.current_thread()))


def main():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
