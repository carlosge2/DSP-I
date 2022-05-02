# Exemplo FFT

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

n = np.arange(16)
ones = np.ones(8)
zeros = np.zeros(8)
x = np.concatenate((ones,zeros))

Y = np.fft.fft(x,16)

print(Y)

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title('signal x(n), 0 <= n <= 15')
axs[0].stem(n, x)
axs[0].grid()
axs[0].set_xlabel("n")

axs[1].set_title("FFT Amplitude, N = 16")
axs[1].stem(n, np.abs(Y))
axs[1].grid()
axs[1].set_xlabel("k")

fig.tight_layout()

plt.show()
