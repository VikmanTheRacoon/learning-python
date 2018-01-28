#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib.request
import time
from bs4 import BeautifulSoup


def main():
    t0 = time.time()
    req = urllib.request.urlopen("http://www.iana.org/domains/reserved")
    t1 = time.time()
    print("\n\n\nTotal Time To Fetch Page: {} Seconds".format(t1 - t0))
    soup = BeautifulSoup(req.read(), "html.parser")
    for link in soup.find_all('a'):
        link.get('href')
    t2 = time.time()
    print("Total Execeution Time: {} Seconds\n\n".format(t2 - t0))


if __name__ == '__main__':

    main()
