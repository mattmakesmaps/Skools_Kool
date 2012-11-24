__author__ = 'matt'

"""
Trying to understand what is the best way to create a class that
should be able to accept a class instance as a construction
parameter.

1. If required by the class, should there be an explicit check
   to ensure that the input argument is an instance of that class?

2. Is there some way to properly use inheritance or composition to
   handle this?
"""

from shapely.geometry import Point

# Create a Point
p1 = Point(10,10)
print p1

# According to Docs, this should work
# And should create a copy of the input point
p2 = Point(p1)
print p2

# Testing copy
p1 = Point(55,55)

print p1
print p2

