from XY_Graph import Graph
from point_module import Point, Point_List, Discrete_Circle
from line_module import Line, Line_List
from Sequence import Pisano, Series

n = 233
m = 4
circle = Discrete_Circle(n)
period = Pisano.pisano_period(n)


polygon_points= Series.newfunc(period)
length = len(polygon_points)

polygons = []
for poly in polygon_points:     #create a Line_List object for each polygon
    polygons.append(Line_List(poly, circle))

dim = Series.calculate_rows_columns(length, m)
x, y = dim
g = Graph(x, y)
g.add_circle()
g.plot_Line_List_List(polygons)
g.show()
i = 0
for ax in g.axes:
    klist = Line_List(polygons[i], circle)
    g.plot_Line_List(klist)
    i = i + 1

print(period)


