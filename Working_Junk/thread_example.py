__author__ = 'matt'

"""
Create a producer function that generates random numbers at a timed interval.
Insert those into a queue
Have a conumer grab products from the queue and perform work.
"""

def producer_ready():
    """Return true to kick off the work"""
    while val
    val = raw_input("Ready >>>")
    return val

if __name__ == '__main__':
    while True:
        if producer_ready():
            product = producer()
            q.insert (0,product)
        if len(q) > 0:
            consumer(q.pop())