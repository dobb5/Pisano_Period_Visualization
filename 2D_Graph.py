import numpy as np
import matplotlib.pyplot as plt
from point_module import Point, Point_List, Discrete_Circle

class Graph:
    """
    A class to represent a graph object.

    Attributes :

    fig : The Figure object representing the graph.
    axes : The axes of the Figure object.
    """

    def __init__(self, n_rows: int = 1, n_cols: int = 1):
        """
        Constructs all the necessary attributes for the Graph object.

        Parameters :
        n_rows(int, optional) : The number of rows of subplots in the Figure object (default is 1).
        n_cols(int, optional) : The number of columns of subplots in the Figure object (default is 1).
        """
        self.fig, self.axes = plt.subplots(nrows=n_rows, ncols=n_cols)
        self.fig.set_figheight(4 * n_rows)
        self.fig.set_figwidth(4 * n_cols)
        self.axes = self.axes.flatten() if isinstance(self.axes, np.ndarray) else [self.axes]

        for ax in self.axes:
            ax.set_aspect(1.0)
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)

    def show(self) -> None:
        """
        Displays the Graph object.
        """
        plt.show()

    def plot(self, arg1, arg2=None):
        """
        Plots a line or a segment on the Graph object.

        Parameters :
        arg1 : If arg2 is None, arg1 is assumed to be a Line object, and a line will be plotted between its two endpoints.
            Otherwise, arg1 and arg2 are assumed to be two Point objects, and a segment will be plotted between them.
        arg2 : The second point for the segment to be plotted (default is None).
        """
        if arg2 is None:
            line = arg1
            p1 = line.a
            p2 = line.b
            x = [p1.x, p2.x]
            y = [p1.y, p2.y]
            self.axes.plot(x, y)
        else:
            p1 = arg1
            p2 = arg2
            x = [p1.x, p2.x]
            y = [p1.y, p2.y]
            self.axes.plot(x, y)

    def add_point(self, point: Point) -> None:
        """
        Adds a Point object to the Graph object.

        Parameters :
        point : The Point object to be added to the Graph object.
        """
        for ax in self.axes:
            ax.plot(point.x, point.y, 'o')
        self.fig.canvas.draw()


    def add_points(self, points: Point_List) -> None:
        """
        Adds a list of Point objects to the Graph object.

        Parameters :
        points(Point_List) : The list of Point objects to be added to the Graph object.
        """
        for point in points:
            self.add_point(point)
    
    def add_circle(self, center: Point = (0, 0), radius: float = 1) -> None:
        """
        Adds a circle to the Graph object.

        Parameters :
        center(Point, optional) : The center point of the circle (default is (0, 0)).
        radius(float, optional) : The radius of the circle (default is 1).
        """
        circle = plt.Circle(center, radius, fill=False)
        for ax in self.axes:
            ax.add_artist(circle)
        self.fig.canvas.draw()



g = Graph()
g.add_circle()
circle = Discrete_Circle(7)
g.add_points(circle.points)
g.show()
