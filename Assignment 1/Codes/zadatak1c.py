import matplotlib.pyplot as plt
import numpy as np

def u(n):
    return 0 if n < 0 else 1

def w(n):
    return 0.5**n*(u(n+2)-u(n-2))

def Evw(n):
    return (w(n)+w(-n))/2

def Odw(n):
    return (w(n)-w(-n))/2

array_x = [
    np.vectorize(w),
    np.vectorize(Evw),
    np.vectorize(Odw)
]

dt = 1

data = [
    np.arange(-3, 3 + dt,dt),
    np.arange(-3, 3 + dt, dt),
    np.arange(-3, 3 + dt, dt)
]

values = list(map(
            lambda param: array_x[param[0]](param[1]),
            enumerate(data)))

y_label_list = ["$w[t]$", "$Ev{w[n]}$", "$Od{w[n]}$"]
plot_names = [
    "Osnovni signal",
    "Parni deo signala",
    "Neparni deo"]

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