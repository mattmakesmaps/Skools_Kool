__author__ = 'matt'

"""
Write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one.
"""

# Question, should my rectangle be a descendent of Point?
# That would negate this requirement for import of point, yes?

from Exercise_1 import Point
from Exercise_2 import Rectangle
from copy import deepcopy

def move_rectangle_copy(rect, dx, dy):
    """Return a copy of input rectangle moved by given delta."""
    rect2 = deepcopy(rect)
    rect2.corner.x = rect2.corner.x + dx
    rect2.corner.y = rect2.corner.y + dy
    return rect2

if __name__ == '__main__':
    r1 = Rectangle(0,0,Point(0,0))
    r2 = move_rectangle_copy(r1, 50, 50)
    print r1 is r2
    print r1.corner.x
    print r2.corner.x

