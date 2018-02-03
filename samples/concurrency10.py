#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import time


class myWorker():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.Lock()

    def modifyA(self):
        with self.lock:
            print("Modifying A : RLock Acquired: {}".format(self.lock._is_owned()))
            print("{}".format(self.lock))
            self.a = self.a + 1
            time.sleep(5)

    def modifyB(self):
        with self.lock:
            print("Modifying B : Lock Acquired: {}".format(self.lock._is_owned()))
            print("{}".format(self.lock))
            self.b = self.b - 1
            time.sleep(5)

    def modifyBoth(self):
        with self.lock:
            print("lock acquired, modifying A and B")
            print("{}".format(self.lock))
            self.modifyA()
            print("{}".format(self.lock))
            self.modifyB()
            print("{}".format(self.lock))


def main():
    workerA = myWorker()
    workerA.modifyBoth()


if __name__ == '__main__':
    main()
