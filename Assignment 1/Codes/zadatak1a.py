import matplotlib.pyplot as plt
import numpy as np

def u(t):
    return 0 if t < 0 else 1

def array_u(t):
    return np.where(t < 0, 0, 1)

def x(t):
    return 5/3*(2*t+1)*(array_u(t+0.5)-array_u(t-1))

array_x = [
    x,
    lambda t: x(t+15),
    lambda t:x(15-t)
]

dt = 0.01

data = [
    np.arange(-1, 2 + dt,dt),
    np.arange(-16, -13 + dt, dt),
    np.arange(13, 16 + dt, dt)
]

values = list(map(
            lambda param: array_x[param[0]](param[1]),
            enumerate(data)))

y_label_list = ["$x(t)$", "$x_p(t)$", "$f(t)$"]
plot_names = [
    "Pocetni signal",
    "Pomeren pocetni signal",
    "Invertovan pomereni signal - konacni"]

plt.style.use('_mpl-gallery')

resolution = 3
plot_count = 3
csfont = {'fontname' : 'Times New Roman', 'fontsize' : 40}
fig, ax = plt.subplots(plot_count,
    figsize=(resolution*4, 2*resolution*plot_count),
    constrained_layout=True)
for i in range(plot_count):
    lx = min(data[i])
    hx = max(data[i])
    ly = min(values[i])
    hy = max(values[i])
    ax[i].set_title(plot_names[i], fontdict=csfont)
    ax[i].xaxis.set_tick_params(labelsize=20)
    ax[i].yaxis.set_tick_params(labelsize=20)
    ax[i].set(xlim=(lx, hx),
              xticks=np.arange(lx, hx, 0.5),
              ylim=(ly, hy+0.5),
              yticks=np.arange(ly, hy+0.5))
    ax[i].plot(data[i], values[i], linewidth=1.5)
    ax[i].axhline(0, color="black")
    ax[i].axvline(0, color="black")
    ax[i].set_xlabel("$t$", fontdict=csfont, fontsize=30)
    ax[i].set_ylabel(
        y_label_list[i], fontdict=csfont, fontsize=30)

plt.show()
