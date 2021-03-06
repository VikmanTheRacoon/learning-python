#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random


class Publisher(threading.Thread):
    def __init__(self, integers, condition):
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self)

    def run(self):
        while True:
            integer = random.randint(0, 1000)
            self.condition.acquire()
            print("Condition Acquired by Publisher: {}".format(self.name))
            self.integers.append(integer)
            print("Publisher {} appending to array: {}".format(self.name, integer))
            self.condition.notify()
            self.condition.release()
            print("Condition Released by Publisher: {}".format(self.name))
            time.sleep(1)


class Subscriber(threading.Thread):
    def __init__(self, integers, condition):
        self.integers = integers
        self.condition = condition
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.condition.acquire()
            print("Condition Acquired by Consumer: {}".format(self.name))
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print("{} Popped from list by Consumer: {}".format(integer, self.name))
                    break
                print("Condition Wait by {}".format(self.name))
                self.condition.wait()
            print("Consumer {} releasing condition".format(self.name))
            self.condition.release()


def main():
    integers = []
    condition = threading.Condition()
    pub1 = Publisher(integers, condition)
    pub1.start()
    sub1 = Subscriber(integers, condition)
    sub2 = Subscriber(integers, condition)
    sub1.start()
    sub2.start()
    sub1.join()
    sub2.join()
    pub1.join()


if __name__ == '__main__':
    main()
