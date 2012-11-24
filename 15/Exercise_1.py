__author__ = 'matt'

from math import sqrt

class Point(object):
    """Represents a 2d Object"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def coord(self):
        return [self.x,self.y]

    def __str__(self):
        return 'Point: %s, %s' % (self.x, self.y)

    def __add__(self, other): # It's convention to use self, other. Other is another instance.
        """Return sum of two coordinates.
           An example of operator overloading."""
        if isinstance(other, Point): # Assume a Point
            sumX = self.x + other.x
            sumY = self.y + other.y
        else: # Assume a tuple
            sumX = self.x + other[0]
            sumY = self.y + other[1]
        return Point(sumX, sumY)

    def __radd__(self, other):
        return self.__add__(other)


def distance_between_points(p1, p2):
    """Return distance between two points"""
    try:
        distance = sqrt(((p2.x - p1.x)**2) + ((p2.y - p1.y)**2))
        return distance
    except Exception, e:
        print 'Error: %s' % e

if __name__ == '__main__':
    myP1 = Point(10,99.9999)
    myP2 = Point(10,15)
    myTuple = (22,22)

    print distance_between_points(myP1,myP2)
    print myP2
    # Operator Overload
    print myP1 + myP2
    print type(myP1 + myP2)
    # Use __add__
    print myP1 + myTuple
    print type(myP1 + myTuple)
    # Use __radd__
    print myTuple + myP1
    print type(myTuple + myP1)

