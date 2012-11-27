__author__ = 'matt'
"""TODO: Shit's Broke"""
"""
Create a producer function that generates random numbers at a timed interval.
Insert those into a queue
Have a conumer grab products from the queue and perform work.
"""

import random, time

def producer_ready():
    """Return true to kick off the work"""
    return 'go'

def producer():
    """Return a random number every set interval of time."""
    for i in range(100):
        time.sleep(1)
        return random.randint(1,1000)

def consumer(a):
    """return a square"""
    time.sleep(4)
    return a**2

if __name__ == '__main__':
    q = []

    while True:
        if producer_ready() == 'go':
            product = producer()
            q.insert (0,product)
            print q
        if len(q) > 0:
            print consumer(q.pop())