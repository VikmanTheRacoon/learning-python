#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()


if __name__ == '__main__':

    main()
