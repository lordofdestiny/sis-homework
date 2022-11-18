import matplotlib.pyplot as plt
import numpy as np
import math

def ak(k):
    k = abs(k)
    if k == 0:
        return 0.5
    elif k % 2 == 0:
        return 1/(k*math.pi)
    else:
        kpi = k*math.pi
        return 1/(kpi**2)*math.sqrt(4+kpi**2)

dt = 1
data = np.arange(-3, 3 + dt, dt)
values = np.vectorize(ak)(data)

plt.style.use('_mpl-gallery')
resolution, plot_count = 3, 1
csfont = {'fontname': 'Times New Roman', 'fontsize': 40}

fig, ax = plt.subplots(plot_count,
                       figsize=(resolution * 4, 2 * resolution * plot_count),
                       constrained_layout=True)
lx,hx = min(data),max(data)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.set(xlim=(lx-1, hx+1), xticks=np.arange(lx, hx + 1),
       ylim=(0, 0.5), yticks=np.arange(0, 1.1,0.1))
markerline, stemline, baseline, = ax.stem(data, values)
ax.axhline(0, color="black")
ax.axvline(0, color="black")
ax.set_xlabel("$k$", fontdict=csfont, fontsize=30)
ax.set_ylabel("$|a_k|$", fontdict=csfont, fontsize=30)
plt.setp(stemline, linewidth=2, color="red")
plt.setp(markerline, markersize=10, color="black")

plt.show()
