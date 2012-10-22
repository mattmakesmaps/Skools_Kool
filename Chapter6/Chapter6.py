# coding=utf-8
__author__ = 'matt'
from math import sqrt

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    else:
        print 'Error!'

def hypotenuse1(leg1, leg2):
    """
    returns the length of the hypotenuse of a right triangle given
    the lengths of the two legs as arguments.
    """
    print leg1, leg2
    return 1

def hypotenuse2(x,y):
    """
    returns the length of the hypotenuse of a right triangle given
    the lengths of the two legs as arguments.
    """
    x2 = x**2
    y2 = y**2

    print x2, y2
    return 1

def hypotenuse3(x,y):
    """
    returns the length of the hypotenuse of a right triangle given
    the lengths of the two legs as arguments.
    """
    x2 = x**2
    y2 = y**2

    sum = x2+y2
    print sum
    return 1

def hypotenuse4(x,y):
    """
    returns the length of the hypotenuse of a right triangle given
    the lengths of the two legs as arguments.
    """
    x2 = x**2
    y2 = y**2

    sum = x2+y2
    hypotenuse = sqrt(sum)
    print hypotenuse
    return hypotenuse

def hypotenuse(x,y):
    """
    returns the length of the hypotenuse of a right triangle given
    the lengths of the two legs as arguments.
    """
    x2 = x**2
    y2 = y**2
    sum = x2+y2
    hypotenuse = sqrt(sum)
    return hypotenuse

def is_between(x,y,z):
    """returns True if x ≤ y ≤ z or False otherwise"""
    #return y >= x and y <=z
    return x <= y <= z # don't need the 'and' for compound compare

if __name__ == '__main__':
    print "Begin 6.1 Exercise 1"
    print compare(5,7)
    print "Begin 6.2 Exercise 2"
    """
    # Incremental development steps
    print hypotenuse1(3,4)
    print hypotenuse2(3,4)
    print hypotenuse3(3,4)
    print hypotenuse4(3,4)
    """
    print hypotenuse(3,4)
    print "Begin 6.4 Exercise 3"
    print is_between(9,1,22)
    print is_between(10,15,20)
