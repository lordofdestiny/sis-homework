from cmath import exp, pi, sin

j = complex(0, 1)


def ddf(t):
    epsilon = 10
    return 1 if abs(t) < epsilon else 0

# def ddf(t):
#     return 1 if t == 0 else 0


def u(t):
    return 1 if t > 0 else 0


def sinc(t):
    return 1 if t == 0 else sin(t) / t


def y1(t):
    return sin(2000 * pi * t) * exp(-100 * t) * u(t)


def y2(t):
    return u(t) - 2 * u(t - 5e-4) + u(t - 1e-3)


# def Y1(w):
#     return 2000 * pi / (100 ** 2 + 200 * j * w - w ** 2 + (2000 * pi) ** 2)

def Y1(w):
    return 1/2/j*(1/(100+j*(w-2000*pi))-1/(100+j*(w+2000*pi)))


def Y2(w):
    return 4 * 0.00025 ** 2 * w * sinc(0.00025 * w) ** 2


def makeLPF(w):
    return lambda x: 1 if abs(x) < w else 0


def makeBPF(w1, w2):
    return lambda x: 1 if w1 < abs(x) < w2 else 0


def modulate(w0):
    return lambda w: pi*(ddf(w-w0)+ddf(w+w0))