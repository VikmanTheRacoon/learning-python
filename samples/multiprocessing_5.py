#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing
import queue
import time


class MyWorker(multiprocessing.Process):
    def __init__(self, stop_event, message_queue):
        super().__init__()
        self.stop_event = stop_event
        self.message_queue = message_queue

    def run(self):
        print('{} {} - Starts'.format(multiprocessing.current_process().name,
                                      multiprocessing.current_process().pid))
        #
        # Loop as long as the stop event is not set
        #
        while not self.stop_event.is_set():
            self.__process_one_message()
        #
        # Loop as long as the queue message is not empty
        #
        print('{} {} - Trying to empty message queue'.format(multiprocessing.current_process().name,
                                                             multiprocessing.current_process().pid))
        while not self.message_queue.empty():
            self.__process_one_message()
        print('{} {} - Stops'.format(multiprocessing.current_process().name,
                                     multiprocessing.current_process().pid))

    def __process_one_message(self):
        try:
            message = self.message_queue.get_nowait()
            print('{} {} - extracted message: {}'.format(multiprocessing.current_process().name,
                                                         multiprocessing.current_process().pid,
                                                         message))
        except queue.Empty:
            print('{} {} - Empty queue'.format(multiprocessing.current_process().name,
                                               multiprocessing.current_process().pid))
            pass


def main():
    message_queue = multiprocessing.Queue()
    stop_event = multiprocessing.Event()
    my_worker = MyWorker(stop_event, message_queue)
    print('{} {} - Asking worker to start'.format(multiprocessing.current_process().name,
                                                  multiprocessing.current_process().pid))
    my_worker.start()
    print('{} {} - Worker started'.format(multiprocessing.current_process().name,
                                          multiprocessing.current_process().pid))
    print('{} {} - Starting to feed message queue'.format(multiprocessing.current_process().name,
                                                          multiprocessing.current_process().pid))
    for i in range(10):
        message_queue.put('Message {}'.format(i))
    print('{} {} - Queue has been fed'.format(multiprocessing.current_process().name,
                                              multiprocessing.current_process().pid))
    print('{} {} - Asking worker to stop'.format(multiprocessing.current_process().name,
                                                 multiprocessing.current_process().pid))
    stop_event.set()
    print('{} {} - Stop event set. Waiting for worker to stop'.format(multiprocessing.current_process().name,
                                                                      multiprocessing.current_process().pid))
    my_worker.join()
    print('{} {} - Worker has stop'.format(multiprocessing.current_process().name,
                                           multiprocessing.current_process().pid))


if __name__ == '__main__':
    main()
