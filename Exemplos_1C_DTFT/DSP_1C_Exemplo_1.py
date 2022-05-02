import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np


#exemplo 1
nd=1
w = np.arange(0,501)*np.pi/500
X = np.exp(-1j*w*nd)

fig, axs = plt.subplots(nrows=2, ncols=2)
axs[0, 1].set_title("parte real")
axs[0, 1].plot(w/np.pi,np.real(X))
axs[0, 1].grid()
axs[0, 1].set_xlabel("frequência em unidades de pi")

axs[1, 1].set_title("parte imaginaria")
axs[1, 1].plot(w/np.pi,np.imag(X))
axs[1, 1].grid()
axs[1, 1].set_xlabel("frequência em unidades de pi")

axs[0, 0].set_title("magnitude")
axs[0, 0].plot(w/np.pi,np.abs(X))
axs[0, 0].grid()
axs[0, 0].set_xlabel("frequência em unidades de pi")

axs[1, 0].set_title("fase")
axs[1, 0].plot(w/np.pi,np.angle(X))
axs[1, 0].grid()
axs[1, 0].set_xlabel("frequência em unidades de pi")

fig.tight_layout()
plt.show()