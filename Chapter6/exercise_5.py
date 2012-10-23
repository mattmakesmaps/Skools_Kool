__author__ = 'matt'

def ack(m,n):
    """Evaluate input based on Ackermann Function"""
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m,n-1))

if __name__ == '__main__':
    print ack(3,2)