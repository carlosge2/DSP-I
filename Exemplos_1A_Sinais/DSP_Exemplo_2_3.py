import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np


#exemplo 2.3

n = np.arange(-10,11)
alpha = -0.1+0.3j
x = np.exp(alpha*n)

fig, axs = plt.subplots(nrows=2, ncols=2)
axs[0, 0].set_title("parte real")
axs[0, 0].stem(n,np.real(x))
axs[0, 0].set_xlabel("n")

axs[0, 1].set_title("parte imaginaria")
axs[0, 1].stem(n,np.imag(x))
axs[0, 1].set_xlabel("n")

axs[1, 0].set_title("parte magnitude")
axs[1, 0].stem(n,np.abs(x))
axs[1, 0].set_xlabel("n")

axs[1, 1].set_title("parte fase")
axs[1, 1].stem(n,np.angle(x))
axs[1, 1].set_xlabel("n")

fig.tight_layout()


plt.show()