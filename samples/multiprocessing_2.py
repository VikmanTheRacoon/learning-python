#!/usr/bin/env python
# -*- coding: utf-8 -*-


import multiprocessing
import time
import random


def worker_process():
    print("Process started: {}".format(multiprocessing.current_process()))
    time.sleep(random.randint(3, 6))
    print("Process terminated: {}".format(multiprocessing.current_process()))


def main():
    print("Main process: {}".format(multiprocessing.current_process()))
    my_process = multiprocessing.Process(target=worker_process)
    my_process.daemon = True
    my_process.start()
    print("We can carry on as per usual and our daemon will continue to execute")
    time.sleep(10)


if __name__ == '__main__':
    main()
