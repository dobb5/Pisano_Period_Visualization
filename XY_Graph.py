import numpy as np
import matplotlib.pyplot as plt
from point_module import Point, Point_List, Discrete_Circle
from line_module import Line_List, Line

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
        color = "#8d57a8"
        self.fig, self.axes = plt.subplots(nrows=n_rows, ncols=n_cols)
        self.fig.patch.set_facecolor(color)  # Light purple color
        self.fig.set_figheight(2 * n_rows)
        self.fig.set_figwidth(2 * n_cols)
        self.axes = self.axes.flatten() if isinstance(self.axes, np.ndarray) else [self.axes]

        for ax in self.axes:
            ax.set_aspect(1.0)
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            ax.set_facecolor(color)
            # Hide x and y axes
            ax.spines['left'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            
            # Hide top and right borders
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            # Hide ticks and tick labels
            ax.set_xticks([])
            ax.set_yticks([])
            ax.xaxis.set_tick_params(size=0)
            ax.yaxis.set_tick_params(size=0)
        

    def show(self) -> None:
        """
        Displays the Graph object.
        """
        plt.show()

    def plot(self, arg1, arg2=None, ax=None):
        if arg2 is None:
            line = arg1
            p1 = line.a
            p2 = line.b
            ax.plot([p1.x, p2.x], [p1.y, p2.y], color="black")
        else:
            p1 = arg1
            p2 = arg2
            ax.plot([p1.x, p2.x], [p1.y, p2.y], color="black")


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
    
    def plot_Line_List(self, lst: Line_List, ax=None):
        if ax is None:
            ax = self.axes[0]  # Use the first axes if ax is not provided

        for line in lst.lines:
            self.plot(line, ax=ax)
    
    def plot_Line_List_List(self, lst_list):
        num_plots = min(len(lst_list), len(self.axes))  # Number of plots to be displayed
        for i in range(num_plots):
            line_list = lst_list[i]
            ax = self.axes[i]  # Get the corresponding axes
            self.plot_Line_List(line_list, ax=ax)

    def add_circle(self, center: Point = (0, 0), radius: float = 1) -> None:
        """
        Adds a circle to the Graph object.

        Parameters :
        center(Point, optional) : The center point of the circle (default is (0, 0)).
        radius(float, optional) : The radius of the circle (default is 1).
        """
        
        for ax in self.axes:
            circle = plt.Circle(center, radius, fill=False)
            ax.add_artist(circle)
        self.fig.canvas.draw()
