from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()

# Exercises 4.3.1-4.3.2
def square(t=bob, length=200):

    """Given a turtle and length, create a square"""
    for i in range(4):
        fd(t, length)
        lt(t)

# Exercise 4.3.3
def polygon(t=bob, length=90, n=5):
    """Given a turtle,length,and number of sides, create a polygon"""
    angle = 360/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

# Exercise 4.3.4
def circle(t=bob, r=50, n=10):
    """Given a turtle and radius, approximate a circle"""
    circumference = 2*pi*r
    print circumference
    length = circumference/n

    polygon(t,length,n)

# Exercise 4.3.5
def arc(t=bob, r=50, angle=270):
    """Given a turtle, radius, and angle approximate a circle.
       Stole this one from the exercise key."""
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

arc()
