#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor


def multiply_by_two(n):
    return n * 2


def main():
    print('\n')
    print('Starting ThreadPoolExecutor')
    values = [2, 3, 4, 5, 6, 7, 8]
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(multiply_by_two, values)
    for result in results:
        print(result)
    print('All tasks complete')


if __name__ == '__main__':
    main()
