#!/usr/bin/env python
# -*- coding: utf-8 -*-


import multiprocessing
import time


def my_worker():
    current_process = multiprocessing.current_process()
    print("Child Process PID: {}".format(current_process.pid))
    time.sleep(20)


def main():
    current_process = multiprocessing.current_process()
    print("Main process PID: {}".format(current_process.pid))
    myProcess = multiprocessing.Process(target=my_worker)
    myProcess.start()
    print("My Process has terminated, terminating main thread")
    print("Terminating Child Process")
    myProcess.terminate()
    print("Child Process Successfully terminated")


if __name__ == '__main__':
    main()
