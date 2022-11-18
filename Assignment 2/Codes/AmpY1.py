import numpy as np
import functions as sig
from math import pi
from drawer import Graph, MyPlotter

w_range, dt = 6000, 1
data = np.arange(-w_range * pi, w_range * pi + dt, dt)


g1 = Graph(data, None, lambda x: abs(sig.Y1(x)),
           xlabel=r"$\omega [ \pi \ \frac{rad}{s} ]$",
           title=r"$|Y_1(j\omega)|$", color="red")

plotter = MyPlotter(plot_count=1)
plotter.add_graph(g1)
plotter.prepare()
plotter.render()