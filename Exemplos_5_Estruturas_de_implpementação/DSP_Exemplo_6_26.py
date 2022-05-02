# Exemplo 6.26

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from fDSP_filtros import QCoeff
from plot_zplane import zplane


r = 0.9
t1 = np.arange(-55,-30,5)
t2 = np.arange(35,60,5)
theta = (np.pi/180)*np.concatenate((t1,t2))

p = r*np.exp(1j*theta)
a = np.poly(p)
b = [1,0]

# Direct form: quantized coefficients
N = 15
[ahat,L,B] = QCoeff(a,N)

# Comparison of Pole-Zero Plots
plt.figure()
frase = "Precisão infinita (FD)"
plt.title(frase)
[HZ,HP,Hl] = zplane(b,a)

plt.figure()
frase1 = "Precisão "+ str(int(1+L+B))+" bits (1+"+str(int(L))+ "+"+str(int(B))+") (FD)"
plt.title(frase1)
[HZ,HP,Hl] = zplane(b,ahat)


# Cascade form: quantized coefficients: Same N
sos = signal.tf2sos(b,a)
[soshat1,L1,B1] = QCoeff(sos,N)
[bhat1,ahat1] = signal.sos2tf(soshat1)

plt.figure()
frase2 = "Precisão "+ str(int(1+L1+B1))+" bits (1+"+str(int(L1))+ "+"+str(int(B1))+") (FC)"
plt.title(frase2)
[HZ,HP,Hl] = zplane(bhat1,ahat1)

# Cascade form: quantized coefficients: Same B (N=L1+B)
N1 = L1+B
#sos = signal.tf2sos(b,a)
[soshat2,L2,B2] = QCoeff(sos,N1)
[bhat2,ahat2] = signal.sos2tf(soshat2)

plt.figure()
frase3 = "Precisão "+ str(int(1+L2+B2))+" bits (1+"+str(int(L2))+ "+"+str(int(B2))+") (FC)"
plt.title(frase3)
[HZ,HP,Hl] = zplane(bhat2,ahat2)

plt.show()