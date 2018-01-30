#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time


def worker():
    print("Thread entered 'Runnig' state")
    # Entering 'Not runnable' state
    time.sleep(3)
    # Thread completes its task and terminates
    print("Thread is terminating")


def main():
    # At this point in time, the thread has no state
    # it hasn't been allocated any system resources
    t = threading.Thread(target=worker)
    # When we call myThread.start(), Python allocates
    # the necessary system
    # resources in order for our thread to run and
    # then calls the thread's # run method.
    # It goes from 'Starting' state to 'Runnable'
    # but not running
    t.start()
    # Here we join the thread and when this method
    # is called # our thread goes into a 'Dead' state.
    # It has finished the job that it was intended to do.
    t.join()
    print("Thead has entered a 'Dead' state")


if __name__ == '__main__':
    main()
