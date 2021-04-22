from PIL import Image, ImageDraw
import sys
from random import randint, choice

import os,sys 

from geometry.shapes.point import Point

class ShapeCollection:
    """ Collection of Shapes """

    def __init__(self):
        self.allpoints = []

    def addshape(self, shape):
        """ adds a shape to the collection """
        self.allpoints.append(shape)

    
    def add_random_points(self, n=100, max_x=100, max_y=100):
        """ adds random points to the shape collection 
            Parameters:
                - n: Number of Points
                - max_x: Maximum x-value to be chosen
                - max_y: Maximum y-value to be chosen
        """
        for _ in range(n):
            self.addshape(Point(randint(0, max_x), randint(0, max_y)))

    
    def _get_dimensions(self):
        """ returns the maximum values of x and y """
        max_x = max([p.x for p in self.allpoints])
        max_y = max([p.y for p in self.allpoints])
        return (max_x, max_y)


    def render_points(self):
        """ creates an image of the points """
        colors = ["red", "green", "blue", "yellow", "black"]
        im = Image.new("RGB", self._get_dimensions(), "#ddd")

        draw = ImageDraw.Draw(im)
        
        for p in self.allpoints:
            draw.point((p.x, p.y), fill=choice(colors))
            
            
        im.save("points.png")

  