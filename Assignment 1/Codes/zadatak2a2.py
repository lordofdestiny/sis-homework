import matplotlib.pyplot as plt
import numpy as np

def z(t):
    if t < -2.5 or t >= 1:
        return 0
    elif -2.5 <= t < -1.5:
        return 5 / 3 * (t ** 2 + 5 * t + 6.25)
    elif -1.5 <= t < -1:
        return 5 / 6 * (t ** 2 + 7 * t + 10.25)
    elif -1 <= t < -0.5:
        return 5 / 6 * (-t ** 2 - 3 * t + 2.25)
    elif -0.5 <= t < 0:
        return 5 / 3 * (-t ** 2 - 2 * t + 1)
    elif 0 <= t < 1:
        return 5 / 6 * (2 - t ** 2 - t)
    else:
        return 0

dt = 0.005

data = np.arange(-3.5, 1.5 + dt, dt)
values = np.vectorize(z, otypes=[float])(data)

plt.style.use('_mpl-gallery')

resolution = 4
plot_count = 1
csfont = {'fontname': 'Times New Roman', 'fontsize': 40}
fig, ax = plt.subplots(plot_count,
                       figsize=(resolution * 3,2 * resolution * plot_count),
                       constrained_layout=True)
lx = min(data)
hx = max(data)
ly = min(values)
hy = max(values)
ax.set_title("Rezultat konvolucije", fontdict=csfont)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.set(xlim=(lx, hx),
       xticks=np.arange(lx, hx + dt),
       ylim=(ly, hy + 0.5),
       yticks=np.arange(ly, hy + 0.5,0.5))
ax.plot(data, values, linewidth=1.5)
ax.axhline(0, color="black")
ax.axvline(0, color="black")
ax.set_xlabel("$t$", fontdict=csfont, fontsize=30)
ax.set_ylabel("$z(t)$", fontdict=csfont, fontsize=30)

plt.show()
