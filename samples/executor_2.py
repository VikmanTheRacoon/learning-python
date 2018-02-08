#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor


def task(n):
    print('Processing {}'.format(n))


def main():
    print('\n')
    print('Starting ThreadPoolExecutor')
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(task, 3)
        executor.submit(task, 5)
        executor.submit(task, 2)
    print('All tasks complete')


if __name__ == '__main__':
    main()
