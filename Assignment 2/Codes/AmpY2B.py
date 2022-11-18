import numpy as np
from cmath import exp, pi
import matplotlib.ticker as ticker
import signals as sig
from drawer import Graph, MyPlotter

j = complex(0, 1)

w_range, dw = 25000, 10
data = np.arange(-w_range*pi, w_range*pi + dw, dw)

g1 = Graph(data, generator=lambda t: abs(sig.Y2B(t)),
           xlabel=r"$\omega [ \pi \ \frac{rad}{s} ] $",
           title=r"|$Y_2^B(j\omega)|$", color="gold")

plotter = MyPlotter(plot_count=1)
plotter.add_graph(g1)
plotter.prepare(5000*pi)
plotter.render()
