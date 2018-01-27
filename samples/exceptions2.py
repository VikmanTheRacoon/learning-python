#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    try:
        f = open('myfileimp.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    main()
