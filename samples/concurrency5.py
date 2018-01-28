#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import time


def main():
    t0 = time.time()
    request = urllib.request.urlopen("http://www.iana.org/domains/reserved")
    page_html = request.read()
    t1 = time.time()
    print("\n\nTotal Time To Fetch Page: {} Seconds\n\n".format(t1 - t0))


if __name__ == '__main__':
    #
    # Call the main() function
    #
    main()
