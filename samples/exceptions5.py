#!/usr/bin/env python
# -*- coding: utf-8 -*-


def echouer():
    x = 1 / 0


def main():
    try:
        echouer()
    except ZeroDivisionError as err:
        print('Interception d\'une runtime error :', err)


if __name__ == '__main__':
    main()
