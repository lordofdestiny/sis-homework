import matplotlib.ticker as ticker
import numpy as np
from math import pi


class Graph:
    def __init__(self, data, values=[], generator=None, xlabel="", title="",
                 color="black", ticks_x=ticker.FuncFormatter(lambda x, pos: f'${(x / pi):g}$')):
        self.data = data
        if generator is None:
            if values is None and len(values) != len(data):
                raise ValueError("You need to provide a generator or a value list")
            self.values = values
        else:
            try:
                self.values = generator(data)
            except ValueError:
                try:
                    self.values = np.vectorize(generator)(data)
                except ValueError:
                    raise ValueError("Generator was not a valid funciton")

        self.xlabel = xlabel
        self.title = title
        self.color = color
        self.ticks_x=ticks_x


class MyPlotter:
    import matplotlib.pyplot as plt
    font = {'fontname': 'Times New Roman', 'fontsize': 40}
    style = 'seaborn-whitegrid'
    plt.style.use(style)

    graphs = []

    lx = 0
    hx = 0
    ly = 0
    hy = 0

    def __init__(self, plot_count=1, resolution=4):
        self.resolution = resolution
        self.plot_count = plot_count
        self.figsize = (self.resolution*4, 2*resolution*self.plot_count)
        self.fig, ax = self.plt.subplots(self.plot_count,
                               figsize=self.figsize,
                               constrained_layout=True)

        self.ax = ax if plot_count > 1 else [ax]

    def add_graph(self, graph):
        self.graphs.append(graph)

    def prepare(self, divisions=1500*pi):
        self.lx = min(map(lambda g: min(g.data), self.graphs))
        self.hx = max(map(lambda g: max(g.data), self.graphs))
        self.ly = min(map(lambda g: min(g.values), self.graphs))
        self.hy = max(map(lambda g: max(g.values), self.graphs))
        x_ticks1 = np.arange(self.lx, 0, divisions)
        x_ticks2 = np.arange(0, self.hx, divisions)
        x_ticks_all = np.concatenate((x_ticks1, x_ticks2), axis=None)
        for i in range(self.plot_count):
            self.plt.figure(i+1)
            graph = self.graphs[i]
            self.ax[i].xaxis.set_major_formatter(graph.ticks_x)
            self.ax[i].set(xlim=(self.lx, self.hx),
                           ylim=(self.ly, self.hy*1.1),
                           xticks=x_ticks_all)
            self.ax[i].plot(graph.data, graph.values, linewidth=1.5,
                            label=graph.data, color=graph.color)
            self.ax[i].set_title(graph.title, fontdict=self.font)
            self.ax[i].xaxis.set_tick_params(labelsize=20)
            self.ax[i].yaxis.set_tick_params(labelsize=20)
            self.ax[i].axhline(0, color="black")
            self.ax[i].axvline(0, color="black")
            self.ax[i].set_xlabel(graph.xlabel, fontdict=self.font, fontsize=30)
            self.ax[i].plot(1, 0, ">k", ms=10, transform=self.ax[i].get_yaxis_transform(), clip_on=False)
            self.ax[i].plot(0, 1, "^k", ms=10, transform=self.ax[i].get_xaxis_transform(), clip_on=False)

    def render(self):
        self.plt.show()
