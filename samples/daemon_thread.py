#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def standard_thread():
    print("Standard thread started")
    time.sleep(20)
    print("Standard thread stopped")


def daemon_thread():
    i = 1
    while True:
        print("Sending heartbeat signal {}".format(i))
        i += 1
        time.sleep(2)


def main():
    standardThread = threading.Thread(target=standard_thread)
    daemonThread = threading.Thread(target=daemon_thread)
    daemonThread.setDaemon(True)
    standardThread.start()
    daemonThread.start()


if __name__ == '__main__':
    main()
