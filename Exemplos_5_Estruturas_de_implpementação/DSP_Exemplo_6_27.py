# Exemplo 6.27

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from fDSP_filtros import QCoeff,freqz_m
from plot_zplane import zplane


r = 0.9
t1 = np.arange(-55,-30,5)
t2 = np.arange(35,60,5)
theta = (np.pi/180)*np.concatenate((t1,t2))

p = r*np.exp(1j*theta)
a = np.poly(p)
b = [1]

[db,mag,pha,grd,w] = freqz_m(b,a)

# Direct form: quantized coefficients
N = 15
[ahat,L,B] = QCoeff(a,N)

[dbhat,maghat,phahat,grdhat,w] = freqz_m(b,ahat)


# Cascade form: quantized coefficients: Same N
sos = signal.tf2sos(b,a)
[soshat1,L1,B1] = QCoeff(sos,N)
[bhat1,ahat1] = signal.sos2tf(soshat1)

[dbhat1,maghat1,phahat1,grdhat1,w] = freqz_m(bhat1,ahat1)

# Cascade form: quantized coefficients: Same B (N=L1+B)
N1 = L1+B
[soshat2,L2,B2] = QCoeff(sos,N1)
[bhat2,ahat2] = signal.sos2tf(soshat2)
[dbhat2,maghat2,phahat2,grdhat2,w] = freqz_m(bhat2,ahat2)

fig, axs = plt.subplots(nrows=2, ncols=2)
frase = "Precisão infinita (FD)"
axs[0,0].set_title(frase)
axs[0,0].plot(w/np.pi,mag)
axs[0,0].grid()
axs[0,0].set_xlabel("frequência em unidades de pi")
axs[0,0].set_ylabel("|H|")

frase2 = "Precisão "+ str(int(1+L1+B1))+" bits (1+"+str(int(L1))+ "+"+str(int(B1))+") (FC)"
axs[1,0].set_title(frase2)
axs[1,0].plot(w/np.pi,maghat1)
axs[1,0].grid()
axs[1,0].set_xlabel("frequência em unidades de pi")
axs[1,0].set_ylabel("|H|")

frase1 = "Precisão "+ str(int(1+L+B))+" bits (1+"+str(int(L))+ "+"+str(int(B))+") (FD)"
axs[0,1].set_title(frase1)
axs[0,1].plot(w/np.pi,maghat)
axs[0,1].grid()
axs[0,1].set_xlabel("frequência em unidades de pi")
axs[0,1].set_ylabel("|H|")

frase3 = "Precisão "+ str(int(1+L2+B2))+" bits (1+"+str(int(L2))+ "+"+str(int(B2))+") (FC)"
axs[1,1].set_title(frase3)
axs[1,1].plot(w/np.pi,maghat2)
axs[1,1].grid()
axs[1,1].set_xlabel("frequência em unidades de pi")
axs[1,1].set_ylabel("|H|")

fig.tight_layout()

plt.show()