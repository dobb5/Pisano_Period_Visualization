from XY_Graph import Graph
from point_module import Point, Point_List, Discrete_Circle
from line_module import Line, Line_List
from Sequence import Pisano, Series

n = 10
circle = Discrete_Circle(n)
period = Pisano.pisano_period(n)
lst = Line_List(period, circle)
polygons = Series.newfunc(period)
print(len(polygons))

g = Graph()
g.add_circle()


g.plot_Line_List(lst)
g.show()
