# exemplo 4.11

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# a) DTFT

x = np.array([1,1,1,1])
w = np.arange(500)*2*np.pi/500
[w, H] = signal.freqz(x,1,w)
fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Magnitude da DTFT")
axs[0].plot(w/np.pi,np.abs(H))
axs[0].grid()
axs[0].set_xlabel("frequência em unidades de pi")
axs[0].set_ylabel("magnitude")

axs[1].set_title("Fase da DTFT")
axs[1].plot(w/np.pi,np.angle(H))
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("fase (radianos)")

fig.tight_layout()

# b) 4-point DFT

x = np.array([1,1,1,1])
N = 4
#w1 = 2*np.pi/N
k = np.arange(N)
X = np.fft.fft(x,N)

magX = np.abs(X)
phaX = np.angle(X)

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Magnitude da DFT: N=4")
axs[0].plot(w*N/(2*np.pi),np.abs(H),linestyle='dotted')
axs[0].stem(k,magX)
axs[0].grid()
axs[0].set_xlabel("k")
axs[0].set_ylabel("magnitude")

axs[1].set_title("Fase da DFT: N=4")
axs[1].plot(w*N/(2*np.pi),np.angle(H),linestyle='dotted')
axs[1].stem(k,phaX)
axs[1].grid()
axs[1].set_xlabel("k")
axs[1].set_ylabel("fase (radianos)")

fig.tight_layout()

# c) 8-point DFT

x = np.array([1,1,1,1])
zeros = np.zeros(4)
x = np.concatenate((x,zeros))
N = 8
#w1 = 2*np.pi/N
k = np.arange(N)
X = np.fft.fft(x,N)

magX = np.abs(X)
phaX = np.angle(X)

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Magnitude da DFT: N=8")
axs[0].plot(w*N/(2*np.pi),np.abs(H),linestyle='dotted')
axs[0].stem(k,magX)
axs[0].grid()
axs[0].set_xlabel("k")
axs[0].set_ylabel("magnitude")

axs[1].set_title("Fase da DFT: N=8")
axs[1].plot(w*N/(2*np.pi),np.angle(H),linestyle='dotted')
axs[1].stem(k,phaX)
axs[1].grid()
axs[1].set_xlabel("k")
axs[1].set_ylabel("fase (radianos)")

fig.tight_layout()

# c) 16-point DFT

x = np.array([1,1,1,1])
zeros = np.zeros(12)
x = np.concatenate((x,zeros))
N = 16
#w1 = 2*np.pi/N
k = np.arange(N)
X = np.fft.fft(x,N)

magX = np.abs(X)
phaX = np.angle(X)

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Magnitude da DFT: N=16")
axs[0].plot(w*N/(2*np.pi),np.abs(H),linestyle='dotted')
axs[0].stem(k,magX)
axs[0].grid()
axs[0].set_xlabel("k")
axs[0].set_ylabel("magnitude")

axs[1].set_title("Fase da DFT: N=16")
axs[1].plot(w*N/(2*np.pi),np.angle(H),linestyle='dotted')
axs[1].stem(k,phaX)
axs[1].grid()
axs[1].set_xlabel("k")
axs[1].set_ylabel("fase (radianos)")

fig.tight_layout()

plt.show()