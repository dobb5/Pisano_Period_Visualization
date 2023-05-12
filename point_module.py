import numpy as np
from typing import Tuple


class Point:
    """
    Attributes :
    x (float) : x-coordinate of the point
    y (float) : y-coordinate of the point
    """

    def __init__(self, x: float, y: float):
        """
        Initializes a point with the given x and y coordinates and index.

        Parameters :
        x (float) : x-coordinate of the point
        y (float) : y-coordinate of the point
        """
        self.x = x
        self.y = y
   
    
    def __str__(self) -> str:
        """Returns a string representation of the point in the format (x, y).""" 
        return f"({self.x}, {self.y})"
    
    @staticmethod
    def distance_between_points(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """"
        Calculates the Euclidean distance between two points.

        Parameters :
        point1 (Tuple[float, float]): first point as a tuple (x, y)
        point2 (Tuple[float, float]): second point as a tuple (x, y)

        Returns :
        float: the distance between the two points
        """
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    

class Point_List:
    """
    Atributes :
    points(Point[]) : list of Point Objects

    Subclass : Descrete_Circle
    """

    def __init__(self):
        self.points = []
        
    def add_point(self, point):
        self.points.append(point)
        
    def remove_point(self, point):
        self.points.remove(point)
        
    def distance_matrix(self):
        n = len(self.points)
        matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] = matrix[j][i] = self.points[i].distance(self.points[j])
        return matrix
    
    def __str__(self):
        return ", ".join(str(point) for point in self.points)

class Discrete_Circle(Point_List):
    """
    Atributes :
    points(Point[]) : list of Point Objects

    Superclass : PointList
    """
    def __init__(self, num_points: int, radius: float = 1):
        super().__init__()
        for i in range(num_points):
            angle = i * (2*np.pi / num_points)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            self.add_point(Point(x, y))


