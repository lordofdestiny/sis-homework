import numpy as np
from cmath import exp, pi
import matplotlib.ticker as ticker
import signals as sig
from drawer import Graph, MyPlotter

j = complex(0, 1)

w_range, dw = 36000, 10
data = np.arange(-w_range*pi, w_range*pi + dw, dw)

g1 = Graph(data, generator=lambda t: abs(sig.Y2D(t)),
           xlabel=r"$\omega [ 1000\pi \ \frac{rad}{s} ] $",
           title=r"|$Y_2^D(j\omega)|$", color="gold",
           ticks_x=ticker.FuncFormatter(lambda x, pos: f'${(x /1000/ pi):g}$'))

plotter = MyPlotter(plot_count=1)
plotter.add_graph(g1)
plotter.prepare(6000*pi)
plotter.render()
