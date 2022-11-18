import matplotlib.pyplot as plt
import numpy as np
import math

def u(t):
    return 0 if t < 0 else 1

def v(L):
    def vk(t):
        s = 0
        for k in range(-L, L + 1):
            s += (t - 4 * k) * (u(t - 4 * k) - u(t - 4 * k - 2))
        return s

    return vk

def v1(t):
    pi2 = math.pi ** 2
    pih = math.pi / 2
    return 2 / pi2 * math.sqrt(4 + pi2) * math.cos(pih * t + math.atan(pih) - math.pi)

def v2(t):
    pi = math.pi
    return 1/pi*math.cos(pi*t+pi/2)

dt = 0.005

signals = [
    np.vectorize(v(9), otypes=[float]),
    np.vectorize(lambda t: 1/2 + v1(t))
]
data = np.arange(-5, 8 + dt, dt)
values = np.array(list(map(lambda signal: signal(data), signals)))

plt.style.use('_mpl-gallery')
signal_names = ["$v(t)$", "$\\hat{v}_1(t)$"]
signal_colors = ["black","green"]
resolution = 4
plot_count = 1
csfont = {'fontname': 'Times New Roman', 'fontsize': 40}
fig, ax = plt.subplots(plot_count,
                       figsize=(resolution * 4, 2 * resolution * plot_count),
                       constrained_layout=True)
lx = min(data)
hx = max(data)
ly = math.floor(min(map(min, values)))
hy = math.ceil(max(map(max, values)))
ax.set(xlim=(lx, hx),
       xticks=np.arange(lx, hx + dt),
       ylim=(ly - 0.5, hy + 0.5),
       yticks=np.arange(ly - 0.5, hy + 1.5, 0.5))
for i in range(len(signals)):
    ax.plot(data, values[i], linewidth=1.5,
            label=signal_names[i],color=signal_colors[i])

ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.axhline(0, color="black")
ax.axvline(0, color="black")
ax.set_xlabel("$t$", fontdict=csfont, fontsize=30)
plt.legend(title="Signali", fontsize=20, title_fontsize=25)
# ax.set_ylabel("$v(t)$", fontdict=csfont, fontsize=30)

plt.show()
