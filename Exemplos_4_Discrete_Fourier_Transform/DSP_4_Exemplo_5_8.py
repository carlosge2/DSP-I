# Exemplo 5.8: HiRes Spectrum

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# a) DFT com N=10


n = np.arange(100)
x = np.cos(0.48*np.pi*n) + np.cos(0.52*np.pi*n)

n1 = np.arange(10)
y1 = x[:10]

Y1 = np.fft.fft(y1,10)
magY1 = np.abs(Y1[:6])
k1 = np.arange(6)
w1 = 2*np.pi/10*k1

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title('signal x(n), 0 <= n <= 9')
axs[0].stem(n1, y1)
axs[0].grid()
axs[0].set_xlabel("n")

axs[1].set_title("DFT Amplitude, N = 10")
axs[1].stem(w1/np.pi, magY1)
axs[1].grid()
axs[1].set_xlabel("frequencia em unidades de pi")

fig.tight_layout()


# b) DFT com N=100 (zero-padding)

n2 = np.arange(100)
zeros = np.zeros(90)
y2 = np.concatenate((y1,zeros))

Y2 = np.fft.fft(y2,100)
magY2 = np.abs(Y2[:51])
k2 = np.arange(51)
w2 = 2*np.pi/100*k2

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title('signal x(n), 0 <= n <= 9 + 90 zeros')
axs[0].stem(n2, y2)
axs[0].grid()
axs[0].set_xlabel("n")

axs[1].set_title("DFT Amplitude, N = 100")
axs[1].stem(w2/np.pi, magY2)
axs[1].grid()
axs[1].set_xlabel("frequencia em unidades de pi")

fig.tight_layout()

# c) DFT com N=100 

X = np.fft.fft(x,100)
magX = np.abs(X[:51])
k = np.arange(51)
w = 2*np.pi/100*k

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title('signal x(n), 0 <= n <= 99')
axs[0].stem(n, x)
axs[0].grid()
axs[0].set_xlabel("n")

axs[1].set_title("DFT Amplitude, N = 100")
axs[1].stem(w/np.pi, magX)
axs[1].grid()
axs[1].set_xlabel("frequencia em unidades de pi")

fig.tight_layout()


plt.show()

