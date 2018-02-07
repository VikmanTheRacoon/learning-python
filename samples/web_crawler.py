#!/usr/bin/env python
# -*- coding: utf-8 -*-

import queue
import ssl
import threading
from urllib.parse import urlparse
from urllib.request import Request, URLError, urljoin, urlopen

from bs4 import BeautifulSoup


class Crawler(threading.Thread):

    def __init__(self, base_url, links_to_crawl, have_visited, error_links, url_lock):
        threading.Thread.__init__(self)
        print("Web Crawler Worker Started: {}".format(threading.current_thread()))
        self.links_to_crawl = links_to_crawl
        self.have_visited = have_visited
        self.base_url = base_url
        self.url_lock = url_lock
        self.error_links = error_links

    def run(self):
        myssl = ssl.create_default_context()
        myssl.check_hostname = False
        myssl.verify_mode = ssl.CERT_NONE
        while True:
            self.url_lock.acquire()
            print("Queue Size: {}".format(self.links_to_crawl.qsize()))
            link = self.links_to_crawl.get()
            self.url_lock.release()
            if link is None:
                break
            if link in self.have_visited:
                print("Already Visited: {}".format(link))
                break
            try:
                link = urljoin(self.base_url, link)
                req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                response = urlopen(req, context=myssl)
                print("Url {} Crawled with Status: {}".format(response.geturl(), response.getcode()))
                soup = BeautifulSoup(response.read(), "html.parser")
                for atag in soup.find_all('a'):
                    if (atag.get('href') not in self.have_visited) and (urlparse(link).netloc == 'tutorialedge.net'):
                        self.links_to_crawl.put(atag.get('href'))
                    else:
                        print("{} already visited or not part of website".format(atag.get('href')))
                print("Adding {} to crawled list".format(link))
                self.have_visited.append(link)
            except URLError as e:
                print("URL {} threw this error when trying to parse: {}".format(link, e.reason))
                self.error_links.append(link)
            finally:
                self.links_to_crawl.task_done()


def main():
    print("Starting our Web Crawler")
    base_url = 'https://tutorialedge.net'
    number_of_threads = 200
    links_to_crawl = queue.Queue()
    url_lock = threading.RLock()
    links_to_crawl.put(base_url)
    have_visited = []
    crawlers = []
    error_links = []
    for i in range(int(number_of_threads)):
        crawler = Crawler(base_url, links_to_crawl, have_visited, error_links, url_lock)
        crawler.start()
        crawlers.append(crawler)
    for crawler in crawlers:
        crawler.join()
    print("Total Number of Pages Visited {}".format(len(have_visited)))
    print("Total Number of Pages with Errors {}".format(len(error_links)))


if __name__ == '__main__':
    main()
