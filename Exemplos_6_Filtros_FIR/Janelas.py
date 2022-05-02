# Filtro FIR exemplo 7.10

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from fDSP_filtros import freqz_m

w_ham = signal.windows.hamming(60)
n=np.arange(60)

[db,mag,pha,grd,w] = freqz_m(w_ham,1)

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Janela hamming M=60")
axs[0].stem(n,w_ham)
axs[0].grid()
axs[0].set_xlabel("n")
axs[0].set_ylabel("w[n]")

axs[1].set_title("Resposta magnitude em dB")
axs[1].plot(w/np.pi,db)
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("dB")

fig.tight_layout()

plt.show()
