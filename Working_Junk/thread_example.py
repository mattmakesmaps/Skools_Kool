__author__ = 'matt'

"""
Create a producer function that generates random numbers at a timed interval.
Insert those into a queue
Have a conumer grab products from the queue and perform work.
"""

import random, time

def producer_ready():
    """Return true to kick off the work"""
    val = 'stop'
    while val <> 'go':
        val = raw_input("Ready >>>")
    return True

def producer():
    """Return a random number every set interval of time."""
    for i in range(100):
        time.sleep(1)
        return random.random

def consumer(a):
    """return a square"""
    return a**2

if __name__ == '__main__':
    q = []

    while True:
        if producer_ready():
            product = producer()
            q.insert (0,product)
        if len(q) > 0:
            print consumer(q.pop())