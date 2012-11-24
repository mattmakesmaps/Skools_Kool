__author__ = 'matt'

from shapely.geometry import Point

p = Point(0,0).buffer(100)
print p.area