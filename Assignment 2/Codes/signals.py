from functions import *
import numpy as np

fc = 6000
wc = 2*pi*fc
Hn1 = makeLPF(4000*pi)
Hn2 = makeLPF(8000*pi)
Hkv = makeLPF(20000*pi)
HRb1 = makeLPF(4000*pi)
HRb2 = makeBPF(4000*pi, 8000*pi)
Hd2r2 = makeLPF(8000*pi)

y1 = np.vectorize(y1)
y2 = np.vectorize(y2)
Y1 = np.vectorize(Y1)
Y2 = np.vectorize(Y2)
Y1N = np.vectorize(lambda w: Y1(w)*Hn1(w))
Y2N = np.vectorize(lambda w: Y2(w)*Hn2(w))
Y2M = np.vectorize(lambda w: (Y2N(w-wc)+Y2N(w+wc))/2)
YT = np.vectorize(lambda w: Y1N(w) + Y2M(w))
YR = YT
Y2B = Y2M
def Y2D(w):
    return 1/4*Y2N(w-2*wc) + 1/2*Y2N(w) + 1/4*Y2N(w+2*wc)
sinc = np.vectorize(sinc)


def modulateVEC(w0):
    return np.vectorize(modulate(w0))


def integrateInFreq(f,data,low,high,step=0.0001):
    result = np.array([])
    t = low
    progressx = 1
    while t <= high:
        if t/high*100 >= progressx:
            print(f"{progressx}% done")
            progressx += 1
        s = 0
        for w in data:
            s += f(w,t)
        result = np.append(result, s*(data[-1]-data[0])/len(data))
        t += step
    return result
