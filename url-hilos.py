#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from Queue import Queue
from threading import Thread
import urllib2
import time


HOSTS = ["http://www.yahoo.com",
         "http://www.google.com", 
         "http://www.amazon.com",
         "http://www.unsa.edu.ar", 
         "http://www.apple.com",
         "http://www.clarin.com.ar",
         "http://www.eltribuno.com.ar"]


class ThreadUrl(Thread):
    """Threaded Url Grab"""
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        host = self.queue.get()

        url = urllib2.urlopen(host)
        print url.read(1024)

        self.queue.task_done()


def main():
    queue = Queue()
    for host in HOSTS:
        queue.put(host)

    s1 = time.time()
    for i in xrange(len(HOSTS)):
        t = ThreadUrl(queue)
        t.start()

    queue.join()
    t1 = time.time() - s1

    s2 = time.time()
    for host in HOSTS:
        url = urllib2.urlopen(host)
        print url.read(1024)
    t2 = time.time() - s2

    print "Tiempo transcurrido con %s threads: %s segundos" % (len(HOSTS), t1)
    print "Tiempo transcurrido sin threads: %s segundos" % (t2, )

if __name__ == '__main__':
    main()
