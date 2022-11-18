import matplotlib.pyplot as plt
import numpy as np

def u(t):
    return 0 if t < 0 else 1

def v(L):
    def vk(t):
        s = 0
        for k in range(-L, L + 1):
            s += (t - 4 * k) * (u(t - 4 * k) - u(t - 4 * k - 2))
        return s

    return vk

dt = 0.005

data = np.arange(-1, 7 + dt, dt)
values = np.vectorize(v(9), otypes=[float])(data)

plt.style.use('_mpl-gallery')
resolution,plot_count = 4,1
csfont = {'fontname': 'Times New Roman', 'fontsize': 40}
fig, ax = plt.subplots(plot_count,
                       figsize=(resolution * 3, 2 * resolution * plot_count),
                       constrained_layout=True)
lx = min(data)
hx = max(data)
ly = min(values)
hy = max(values)
ax.set_title("Pocetni signal", fontdict=csfont)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.set(xlim=(lx, hx),
       xticks=np.arange(lx, hx + dt),
       ylim=(ly, hy + 2),
       yticks=np.arange(ly, hy + 2))
ax.plot(data, values, linewidth=1.5)
ax.axhline(0, color="black")
ax.axvline(0, color="black")
ax.set_xlabel("$t$", fontdict=csfont, fontsize=30)
ax.set_ylabel("$v(t)$", fontdict=csfont, fontsize=30)

plt.show()
