import matplotlib.pyplot as plt
import numpy as np

def u(n):
    return 0 if n < 0 else 1

def array_u(n):
    return np.where(n < 0, 0, 1)

def w(n):
    return 0.5**n * (array_u(n + 2) - array_u(n - 2))

array_x = [
    w,
    lambda n: w(n - 2),
]

dt = 1

data = [
    np.arange(-3, 3 + dt, dt),
    np.arange(-1, 5 + dt, dt),
]

values = list(map(
    lambda param: array_x[param[0]](param[1]),
    enumerate(data)))

y_label_list = ["$w[n]$", "$w_p[t]=\\frac{1}{2}r[n]$"]
plot_names = [
    "Pocetni signal",
    "Pomeren pocetni signal"]

plt.style.use('_mpl-gallery')

resolution = 3
plot_count = 2
csfont = {'fontname': 'Times New Roman', 'fontsize': 40}
fig, ax = plt.subplots(plot_count,
                       figsize=(resolution * 4, 2 * resolution * plot_count),
                       constrained_layout=True)
for i in range(plot_count):
    lx = min(data[i])
    hx = max(data[i])
    ly = min(values[i])
    hy = max(values[i])
    ax[i].xaxis.set_tick_params(labelsize=20)
    ax[i].yaxis.set_tick_params(labelsize=20)
    ax[i].set_title(plot_names[i], fontdict=csfont)
    ax[i].set(xlim=(lx, hx),
              xticks=np.arange(lx, hx+1),
              ylim=(ly, hy+1),
              yticks=np.arange(ly, hy+1))
    markerline, stemline, baseline,= ax[i].stem(data[i], values[i])
    ax[i].axhline(0, color="black")
    ax[i].axvline(0, color="black")
    ax[i].set_xlabel("$n$", fontdict=csfont, fontsize=30)
    ax[i].set_ylabel(
        y_label_list[i],
        fontdict=csfont,
        fontsize=30)
    plt.setp(stemline, linewidth=2,color="red")
    plt.setp(markerline, markersize=10,color="black")

plt.show()