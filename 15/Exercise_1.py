__author__ = 'matt'

from math import sqrt

class Point(object):
    """Represents a 2d Object"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def coord(self):
        return [self.x,self.y]

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

    print distance_between_points(myP1,myP2)
