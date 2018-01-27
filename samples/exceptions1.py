#!/usr/bin/env python
# -*- coding: utf-8 -*-


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


def main():
    for cls in [B, C, D]:
        try:
            raise cls()
        except B:
            print("B")
        except C:
            print("C")
        except D:
            print("D")


if __name__ == '__main__':
    main()
