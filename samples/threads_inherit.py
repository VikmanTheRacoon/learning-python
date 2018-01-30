#!/usr/bin/env python
# -*- coding: utf-8 -*-


from threading import Thread


class WorkerThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("Thread is now running")


def main():
    worker_thread = WorkerThread()
    print("Created the Thread object")
    worker_thread.start()
    print("Started thread")
    worker_thread.join()
    print("Finished thread")


if __name__ == '__main__':
    main()
