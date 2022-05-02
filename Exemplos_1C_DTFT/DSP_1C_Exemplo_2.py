import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np


#exemplo 2

w = np.arange(0,501)*np.pi/500
X = 0.5*(1+(np.exp(-1j*w)))

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("magnitude")
axs[0].plot(w/np.pi,20*np.log(X))
axs[0].grid()
axs[0].set_xlabel("frequência em unidades de pi")
axs[0].set_ylabel("ganho em decibeis")
axs[0].axis([0,1,-40 ,0])

axs[1].set_title("fase")
axs[1].plot(w/np.pi,np.angle(X))
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("radianos")

fig.tight_layout()



plt.show()