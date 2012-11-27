__author__ = 'matt'

#import swampy.World
#
#world = swampy.World.World() # Swampy is the package, World is a module, containing a World class
#
#canvas = world.ca(width=500, height=500, background='white')
#bbox = [[-150,-100],[150,100]]
#canvas.rectangle(bbox,outline='black',width=2,fill='green4')
#
#world.mainloop()

from swampy import World
from Exercise_2 import Point

class Rectangle(object):
    """Takes two points representing a bbox, and a color"""

    def __init__(self,ll,ur,color='red'):
        assert isinstance(ll, Point)
        assert isinstance(ur, Point)
        self.ll = ll
        self.ur = ur
        self.color = color

    def bbox(self):
        return [self.ll.coord(),self.ur.coord()] # Has to be a better way

def draw_rectangle(canin,rectin):
    """Return a representation of a rectangle on a canvas."""
    """
    Didn't Understand what they were asking. Isn't a rectangle a method inside of the canvas class?

    Looking at Jeff's code, a rectangle is actually an object with a lower-left corner and an upper-right corner.

    OK I get it now, supposed to use previously created rectangle and point classes

    """
    canin.rectangle(rectin.bbox(),outline='black',width=2,fill=rectin.color)

if __name__ == '__main__':

    """
    Write a function called draw_rectangle that takes a Canvas and a Rectangle as arguments and draws a
    representation of the Rectangle on the Canvas.
    """

    world = World.World()
    canvas = world.ca(width=500, height=500, background='white')

    p1 = Point(-175,-85)
    p2 = Point(200,85)
    # would using attributes negate me needing to using function-like calls e.g.
    # p1.coord vs. p1.coord()
    draw_rectRect = Rectangle(p1,p2,'blue')

    draw_rectangle(canvas, draw_rectRect)
    world.mainloop()
