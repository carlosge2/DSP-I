# Exemplo 8.28

import numpy as np
from scipy import signal
from fDSP_filtros import u_buttap,afd_butt,freqs_m,freqz_m,u_chb1ap,afd_chb1,imp_invr
import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
from plot_zplane import zplane

# Digital Highpass Filter Specifications:
wp = 0.6*np.pi    # digital Passband freq in rad
ws = 0.4586*np.pi # digital Stopband freq in rad
Rp = 1            # Passband ripple in dB
As = 15           # Stopband attenuation in dB

# Calculations of Chebyshev-I Filter Parameters:
[N,wn] = signal.cheb1ord(wp/np.pi,ws/np.pi,Rp,As);

# Digital Chebyshev-I Highpass Filter Design:
[b,a] = signal.cheby1(N,Rp,wn,'high')

ep = np.sqrt(10**(Rp/10)-1)     # Passband Ripple parameter
Ripple = np.sqrt(1/(1+ep*ep))   # Passband Ripple
Attn = 1/(10**(As/20))          # Stopband Attenuation

[db,mag,pha,grd,w] = freqz_m(b,a)

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('Resposta em magnitude')
axs[0,0].plot(w/np.pi,mag)
axs[0,0].axhline(Ripple, color='r')
axs[0,0].axhline(Attn, color='r')
axs[0,0].axvline(wp/np.pi, color='r')
axs[0,0].axvline(ws/np.pi, color='r')
axs[0,0].grid()
axs[0,0].set_xlabel("frequência em unidades de pi")
axs[0,0].set_ylabel("|H|")


axs[1,0].set_title("Resposta de fase")
axs[1,0].plot(w/np.pi,pha/np.pi)
axs[1,0].grid()
axs[1,0].set_xlabel("frequência em unidades de pi")
axs[1,0].set_ylabel("radianos")

axs[0,1].set_title("Resposta magnitude em dB")
axs[0,1].plot(w/np.pi,db)
axs[0,1].axhline(-Rp, color='r')
axs[0,1].axhline(-As, color='r')
axs[0,1].axvline(wp/np.pi, color='r')
axs[0,1].axvline(ws/np.pi, color='r')
axs[0,1].grid()
axs[0,1].set_xlabel("frequência em unidades de pi")
axs[0,1].set_ylabel("decibeis")
axs[0,1].axis([0,1,-30,0])

axs[1,1].set_title("Atraso de grupo")
axs[1,1].plot(w/np.pi,grd)
axs[1,1].grid()
axs[1,1].set_xlabel("frequência em unidades de pi")
axs[1,1].set_ylabel("Amostras")

fig.tight_layout()

plt.figure()
plt.title("Diagrama de polos e zeros")
z,p,k = zplane(b,a)

plt.show()


              
              