__author__ = 'matt'
import Queue, random, time

def producer():
    for i in range (100):
        time.sleep(1)
        return random.randint(1,1000)

def consumer(val):
    time.sleep(4)
    return val**2

if __name__ == '__main__':
    q = Queue.Queue()

    while True:
        product = producer()
        print q.qsize()
        q.put(product)

        while not q.empty():
            val = q.get()
            print consumer(val)