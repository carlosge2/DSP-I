# exemplo 4.11

import numpy as np
# If the code is in a file called plot_zplane.py
from plot_zplane import zplane
from scipy import signal
import matplotlib.pyplot as plt

b = np.array([1, 0])
a = np.array([1, -0.9])
zplane(b,a)

[w, H] = signal.freqz(b,a)
fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Resposta em magnitude")
axs[0].plot(w/np.pi,np.abs(H))
axs[0].grid()
axs[0].set_xlabel("frequência em unidades de pi")
axs[0].set_ylabel("magnitude")

axs[1].set_title("Resposta de fase")
axs[1].plot(w/np.pi,np.angle(H))
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("fase (radianos)")

fig.tight_layout()



plt.show()