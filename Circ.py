#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab
import matplotlib.path
import matplotlib.pyplot as plt


def drawCircles (axes):
    """
    Рисование окружностей
    """
    circle1 = pylab.Circle((0, 0), radius=0.1, fill=True)
    axes.add_patch (circle1)
    pylab.text (0, 0.2, "Circle", horizontalalignment="center")

    circle2 = pylab.Circle((0, 0),
                           radius=1.5,
                           fill=False,
                           color="r")
    axes.add_patch (circle2)
    pylab.text (0, 1.55, "Circle", horizontalalignment="center")








def drawPolygons (axes):
    """
    Рисование многоугольника
    """
    polygon_1 = pylab.Polygon ([(0, -0.75),
                                (0, -1.25),
                                (0.5, -1.25),
                                (1, -0.75)])
    axes.add_patch (polygon_1)
    pylab.text (0.6, -0.7, "Polygon", horizontalalignment="center")


    polygon_2 = pylab.Polygon ([(-0.5, 0),
                                (-1, -0.5),
                                (-1, -1),
                                (-0.5, -1)],
                               fill = False,
                               closed = False)
    axes.add_patch (polygon_2)
    pylab.text (-1.0, -0.1, "Polygon", horizontalalignment="center")



if __name__ == "__main__":
    pylab.xlim (-2, 2)
    pylab.ylim (-2, 2)
    pylab.grid()

    # Получим текущие оси
    axes = pylab.gca()
    axes.set_aspect("equal")


    drawPolygons (axes)

    drawCircles (axes)


    plt.show()