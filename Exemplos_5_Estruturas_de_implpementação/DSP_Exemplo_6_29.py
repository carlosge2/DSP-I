# Exemplo 6.29

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from fDSP_filtros import QCoeff,freqz_m
from plot_zplane import zplane

# The following function computes the filter
# coefficients given in Table 6.2.
b = signal.remez(30,np.array([0,0.3,0.5,1])*1/2,np.array([1,0]))
w = np.arange(501)*np.pi/500


[db,mag,pha,grd,w] = freqz_m(b,[1,0])

# quantized coefficients 16 bits
N1 = 15
[bhat1,L1,B1] = QCoeff(b,N1)

[dbhat1,maghat1,phahat1,grdhat1,w] = freqz_m(bhat1,[1,0])


# quantized coefficients 8 bits
N2 = 7
[bhat2,L2,B2] = QCoeff(b,N2)

[dbhat2,maghat2,phahat2,grdhat2,w] = freqz_m(bhat2,[1,0])

plt.figure()
plt.title("Precisão infinita")
[HZ,HP,Hl] = zplane(b,[1,0])

plt.figure()
frase2 = "Precisão "+ str(int(1+L1+B1))+" bits (1+"+str(int(L1))+ "+"+str(int(B1))+")"
plt.title(frase2)
[HZ,HP,Hl] = zplane(bhat1,[1,0])

plt.figure()
frase3 = "Precisão "+ str(int(1+L2+B2))+" bits (1+"+str(int(L2))+ "+"+str(int(B2))+")"
plt.title(frase3)
[HZ,HP,Hl] = zplane(bhat2,[1,0])

fig, axs = plt.subplots(nrows=1, ncols=2)

frase4 = "Magnitude: "+ str(int(1+L1+B1))+" bits (1+"+str(int(L1))+ "+"+str(int(B1))+")"
axs[0].set_title(frase4)
axs[0].plot(w/np.pi,db, 'r', label='inf')
axs[0].plot(w/np.pi,dbhat1,'k',label='16 bits')
axs[0].legend(loc='best')
axs[0].grid()
axs[0].set_xlabel("frequência em unidades de pi")
axs[0].set_ylabel("dB")
axs[0].axis([0,1,-80,5])

frase5 = "Magnitude: "+ str(int(1+L2+B2))+" bits (1+"+str(int(L2))+ "+"+str(int(B2))+")"
axs[1].set_title(frase5)
axs[1].plot(w/np.pi,db,'r', label='inf')
axs[1].plot(w/np.pi,dbhat2,'k',label='8 bits')
axs[1].legend(loc='best')
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("dB")
axs[1].axis([0,1,-80,5])

fig.tight_layout()

plt.show()