#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Lock


class LockedSet(set):
    """A thread-safe Set type implementation
    """

    def __init__(self, *args, **kwargs):
        self.__lock = Lock()
        super(LockedSet, self).__init__(*args, **kwargs)

    def add(self, element):
        with self.__lock:
            super(LockedSet, self).add(element)

    def remove(self, element):
        with self.__lock:
            super(LockedSet, self).remove(element)
