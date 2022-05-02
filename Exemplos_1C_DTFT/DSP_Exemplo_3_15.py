import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold,conv_m
import numpy as np
from scipy import signal

#exemplo 3.15

a=np.array([1,-0.8])
b=np.array([1])
n = np.arange(101)
x=np.cos(0.05*np.pi*n)
y=signal.lfilter(b,a,x)

fig, axs = plt.subplots(nrows=2, ncols=1)
axs[0].set_title("Sequência de entrada")
axs[0].stem(n,x)
axs[0].set_xlabel("n")
axs[0].set_ylabel("x[n]")

axs[1].set_title("Sequência de saída")
axs[1].stem(n,y)
axs[1].set_xlabel("n")
axs[1].set_ylabel("y[n]")
fig.tight_layout()


plt.show()