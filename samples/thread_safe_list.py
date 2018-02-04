#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import RLock


class LockedList(list):
    """A thread-safe List type implementation
    """

    def __init__(self, *args, **kwargs):
        self.__lock = RLock()
        super(LockedList, self).__init__(*args, **kwargs)

    def clear(self):
        with self.__lock:
            super(LockedList, self).clear()

    def append(self, element):
        with self.__lock:
            super(LockedList, self).append(element)

    def extend(self, element):
        with self.__lock:
            super(LockedList, self).extend(element)

    def __setitem__(self, key, value):
        with self.__lock:
            super(LockedList, self).__setitem__(key, value)
