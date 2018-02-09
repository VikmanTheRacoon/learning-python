#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing


def my_worker():
    print("Currently Executing Child Process")
    print("This process has it's own instance of the GIL")
    print("Executing Main Process")
    print("Creating Child Process")


def main():
    my_process = multiprocessing.Process(target=my_worker())
    my_process.start()
    my_process.join()
    print("Child Process has terminated, terminating main process")


if __name__ == '__main__':
    main()
