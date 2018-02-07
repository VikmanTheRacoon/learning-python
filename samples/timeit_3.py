#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import ssl
from urllib.request import Request, urlopen


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = timeit.default_timer

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, *args):
        end = timeit.default_timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs * 1000
        if self.verbose:
            print('elapsed time: {} ms'.format(self.elapsed))


def my_function():
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    with Timer(verbose=True) as t:
        req = Request('https://tutorialedge.net', headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, context=myssl)
    print("Elapsed Time: {} seconds".format(t.elapsed_secs))


def main():
    my_function()


if __name__ == '__main__':
    main()
