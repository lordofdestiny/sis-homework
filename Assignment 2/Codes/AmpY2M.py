import numpy as np
import signals as sig
from cmath import pi, exp
from drawer import Graph, MyPlotter

w_range, dt = 25000, 10
data = np.arange(-w_range * pi, w_range * pi + dt, dt)

g1 = Graph(data,generator=sig.Y2M,
           xlabel=r"$\omega [ \pi \ \frac{rad}{s} ] $",
           title=r"|$Y_2^M(j\omega)|$", color="orange")

plotter = MyPlotter(plot_count=1)
plotter.add_graph(g1)
plotter.prepare(5000*pi)
plotter.render()