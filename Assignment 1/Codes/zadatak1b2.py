import matplotlib.pyplot as plt
import numpy as np

def u(n):
    return 0 if n < 0 else 1

array_u = np.vectorize(u)

def w(n):
    return 0.5 ** n * (array_u(n + 2) - array_u(n - 2))

def r(n):
    return 2 * w(n - 2)

def v(n):
    if n % 3 == 0:
        return r(n // 3)
    elif n % 3 == 1:
        return (2 * r(n // 3) + r(n // 3 + 1)) / 3
    else:
        return (r(n // 3) + 2 * r(n // 3 + 1)) / 3

dt = 1

data = np.arange(-4, 13 + dt, dt)

values = np.vectorize(v)(data)

plt.style.use('_mpl-gallery')

resolution = 3
plot_count = 1
csfont = {'fontname': 'Times New Roman', 'fontsize': 40}
fig, ax = plt.subplots(plot_count,
                       figsize=(resolution * 4, 2 * resolution * plot_count),
                       constrained_layout=True)
lx = min(data)
hx = max(data)
ly = min(values)
hy = max(values)
ax.set_title("Konacni signal", fontdict=csfont)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.set(xlim=(lx, hx), xticks=np.arange(lx, hx + 1),
       ylim=(ly, hy + 1), yticks=np.arange(ly, hy + 1))
markerline, stemline, baseline, = ax.stem(data, values)
ax.axhline(0, color="black")
ax.axvline(0, color="black")
ax.set_xlabel("$n$", fontdict=csfont, fontsize=30)
ax.set_ylabel("$v[n]$", fontdict=csfont, fontsize=30)
plt.setp(stemline, linewidth=2, color="red")
plt.setp(markerline, markersize=10, color="black")

plt.show()
