import numpy as np
import signals as sig
from math import pi
from drawer import Graph, MyPlotter

w_range, dt = 12000, 1
data = np.arange(-w_range * pi, w_range * pi + dt, dt)


g1 = Graph(data, None, lambda x: np.abs(sig.Y1N(x)), xlabel=r"$\omega [ \pi \ \frac{rad}{s} ] $",
           title=r"$|Y_1^N(j\omega)|$", color="red")

plotter = MyPlotter(plot_count=1)
plotter.add_graph(g1)
plotter.prepare(3000*pi)
plotter.render()