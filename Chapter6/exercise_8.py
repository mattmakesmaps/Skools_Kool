# coding=utf-8
__author__ = 'matt'

def gcd(a,b):
    """
    take two numbers and return the greatest
    common divisor.
    """
    if a == b:
        return a
    else:
        values = sorted([a,b])
        return gcd(values[1] - values[0], values[0])

if __name__ == '__main__':
    print gcd(1989,867)
    print gcd(1989,867.0)
