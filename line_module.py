from point_module import Point, Descrete_Circle
import numpy as np
from typing import Tuple

class Line:
    """
    A class representing a line in a two-dimensional space.
    
    Attributes:
        point1 (Point): The first endpoint of the line.
        point2 (Point): The second endpoint of the line.
        
    Methods:
        length: Calculates the length of the line.
        slope: Calculates the slope of the line.
        intersection: Calculates the intersection between two lines.
    """
    
    def __init__(self, point1, point2):
        """Initialize a Line instance with two endpoints."""
        self.a = point1
        self.b = point2
    
    def length(self):
        """Calculate the length of the line."""
        return np.sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2)
    
    def slope(self):
        """Calculate the slope of the line."""
        if self.b.x - self.a.x == 0:
            return None
        else:
            return (self.b.y - self.a.y) / (self.b.x - self.a.x)

    def intersection(line1: Tuple[Point, Point], line2: Tuple[Point, Point]) -> Point:
        """""Uses the determinate to find the intersection between two lines"""""
        x1 = line1.a.x
        x2 = line1.b.x
        x3 = line2.a.x
        x4 = line2.b.x
        y1 = line1.a.y
        y2 = line1.b.y
        y3 = line2.a.y
        y4 = line2.b.y

        denom = (x1 -x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if(denom == 0):
            return None

        x_intersection = (((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom)
        y_intersection = (((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom)
        
        return Point(x_intersection, y_intersection, None)
    
class Line_List:
    """
    A collection of Line objects.

    Attributes:
    -----------
    lines : list
        A list of Line objects.
    """

    def __init__(self):
        """
        Initializes an empty list of lines.
        """
        self.lines = []

    def __init__(self, lst, circle: Descrete_Circle):
        """
        Initializes a list of lines based on a list of points and a circle.

        Parameters :
        lst : A list of integers representing the indices of the points on the circle.
        circle(Descrete_Circle): A Descrete_Circle object representing the circle on which the points lie.
        """
        for i in range(1, len(lst)):
            self.append(Line(circle[lst[i - 1]], circle[lst[i]]))

    def add_line(self, line):
        """
        Adds a Line object to the list.

        Parameters :
        line : The Line object to add.
        """
        self.lines.append(line)
        
    def remove_line(self, line):
        """
        Removes a Line object from the list.

        Parameters :
        line : The Line object to remove.
        """
        self.lines.remove(line)

