import pylab
import matplotlib.patches
import matplotlib.lines
import matplotlib.path
import matplotlib.pyplot as plt
def drawPolygons (axes):
    """
    Рисование многоугольника
    """
    polygon_1 = matplotlib.patches.Polygon ([(0, -0.75), (0, -1.25),(0.5, -1.25),(1, -0.75)])
    axes.add_patch (polygon_1)
    if __name__ == "__main__":
        pylab.xlim(-5, 5)
        pylab.ylim(-1, 100)
        pylab.grid()

        # Получим текущие оси
        axes = pylab.gca()
        axes.set_aspect("equal")
        drawPolygons(axes)
        plt.show()