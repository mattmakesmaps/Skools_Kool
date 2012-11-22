__author__ = 'matt'

"""
Write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy.
It should change the location of the rectangle by adding dx to the x coordinate
of corner and adding dy to the y coordinate of corner.
"""

from Exercise_1 import Point
import copy

class Rectangle(object):
    """Represents a rectangle."""
    def __init__(self, w, h, p=Point(0,0)):
        self.width = w
        self.height = h
        self.corner = p

    def move(self, dx, dy):
        """Shift rectangle based on delta from corner."""
        self.corner.x = self.corner.x + dx
        self.corner.y = self.corner.y + dy


def move_rectangle(rect, dx, dy):
    """Shift a rectangle based on a delta from the corner."""
    rect.corner.x = rect.corner.x + dx
    rect.corner.y = rect.corner.y + dy

if __name__ == '__main__':
    p1 = Point(10,10)
    p2 = Point(0,0)
    r1 = Rectangle(500,500)
    """
    Both r1 and r2 reference the same default Point() instance in the class.
    A change to r1.corner.x will affect r2.corner.x
    """
#    r2 = Rectangle(500,500)

    """
    A deep copy will break the reference to the default Point().
    """
#    r2 = copy.deepcopy(r1)

    """
    A shallow copy will retain a reference to default Point().
    """
#    r2 = copy.copy(r1)

    """
    Explicity assignment r2 to another Point() instance will override the default Point()
    instance in the class.
    """
    r2 = Rectangle(500,500,Point(0,0))

    print 'Start r1.corner.x: %s' % r1.corner.x
    print 'r2.corner.x: %s' % r2.corner.x

    move_rectangle(r1,15,15)

    print 'Function Result r1.corner.x: %s' % r1.corner.x
    print 'r2.corner.x: %s' % r2.corner.x

    r1.move(20,25)

    print 'Method Result r1.corner.x: %s' % r1.corner.x
    print 'r2.corner.x: %s' % r2.corner.x
