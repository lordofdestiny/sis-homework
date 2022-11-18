import numpy as np
import functions as sig
from math import pi
from drawer import Graph, MyPlotter

w_range, dt = 12000, 1
data = np.arange(-w_range * pi, w_range * pi + dt, dt)


g1 = Graph(data, None, lambda x: abs(sig.Y1(x)), xlabel=r"$\omega [ \pi \ \frac{rad}{s} ] $",
           title=r"$Y_1(j\omega)$", color="red")
g2 = Graph(data, None, lambda x: abs(sig.Y2(x)), xlabel=r"$\omega [ \pi \ \frac{rad}{s} ] $",
           title=r"$Y_2(j\omega)$", color="green")

plotter = MyPlotter(plot_count=1)
plotter.add_graph(g2)
plotter.add_graph(g1)
plotter.prepare(3000*pi)
plotter.render()