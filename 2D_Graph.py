import numpy as np
import matplotlib.pyplot as plt
from point_module import Point

class Graph:

    def __init__(self, n_rows=1, n_cols=1):
        self.fig, self.axes = plt.subplots(nrows=n_rows, ncols=n_cols)
        self.fig.set_figheight(4*n_rows)
        self.fig.set_figwidth(4*n_cols)
        self.axes = self.axes.flatten() if isinstance(self.axes, np.ndarray) else [self.axes]
        for ax in self.axes:
            ax.set_aspect(1.0)
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)


    def show(self) -> None:
        plt.show()
        

    def plot(self, arg1, arg2=None):
        if arg2 is None:
            line = arg1
            p1 = line.a
            p2 = line.b
            x = [p1.x, p2.x]
            y = [p1.y, p2.y]
            self.ax.plot(x, y)
        else:
            p1 = arg1
            p2 = arg2
            x = [p1.x, p2.x]
            y = [p1.y, p2.y]
            self.ax.plot(x, y)

    # def add_point(self, point: Point) -> None:
    #     self.ax.plot(point.x, point.y, 'o')
    #     self.fig.canvas.draw()

    
    # def add_points(self, points: list[Point]) -> None:
    #     for point in points:
    #         self.add_point(point)
        
    # def add_circle(self, center: Point = (0, 0), radius: float = 1) -> None:
    #     circle = plt.Circle(center, radius, fill=False)
    #     self.ax.add_artist(circle)
    #     self.fig.canvas.draw()


