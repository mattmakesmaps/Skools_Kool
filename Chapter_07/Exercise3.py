__author__ = 'matt'

from math import sqrt

def test_square_root(a):
    """
    Print number, square root by formula in text,
    square root by math.sqrt, absolute value of difference.
    """
    n=1.0 # Start Value

    while n<a:
        b=5.0 # Guesstimate Value

        print str(n) + " ",

        while True:

            y = (b+n/b) / 2
            if y == b:
                print str(y) + " ",
                break
            b=y

        val = sqrt(n)
        print str(val) + " ",

        print abs(b - val)

        n += 1

if __name__ == '__main__':
    test_square_root(10)