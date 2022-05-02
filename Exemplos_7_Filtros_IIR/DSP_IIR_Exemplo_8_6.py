# Exemplo 8.6

import numpy as np
from scipy import signal
from fDSP_filtros import u_buttap,afd_butt,freqs_m,u_chb1ap,afd_chb1
import matplotlib.pyplot as plt

Wp = 0.2*np.pi
Ws = 0.3*np.pi
Rp = 1
As = 16
Ripple = 10 ** (-Rp/20)
Attn = 10 ** (-As/20)
# Analog filter design
[b,a] = afd_chb1(Wp,Ws,Rp,As)

# Calculation of Frequency Response
[db,mag,pha,w] = freqs_m(b,a,0.5*np.pi)

# Calculation of Impulse response
t,ha = signal.impulse((b,a))

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('Resposta em magnitude')
axs[0,0].plot(w/np.pi,mag)
axs[0,0].grid()
axs[0,0].axhline(Ripple, color='r')
axs[0,0].axhline(Attn, color='r')
axs[0,0].axvline(Wp/np.pi, color='r')
axs[0,0].axvline(Ws/np.pi, color='r')
axs[0,0].set_xlabel("frequência analógica em unidades de pi")
axs[0,0].set_ylabel("|H|")
axs[0,0].axis([0,0.5,0,1.1])

axs[1,0].set_title("Resposta de fase")
axs[1,0].plot(w/np.pi,pha/np.pi)
axs[1,0].grid()
axs[1,0].set_xlabel("frequência analógica em unidades de pi")
axs[1,0].set_ylabel("radianos")
axs[1,0].axis([0,0.5,-1,1])

axs[0,1].set_title("Resposta magnitude em dB")
axs[0,1].plot(w/np.pi,db)
axs[0,1].grid()
axs[0,1].axhline(-Rp, color='r')
axs[0,1].axhline(-As, color='r')
axs[0,1].axvline(Wp/np.pi, color='r')
axs[0,1].axvline(Ws/np.pi, color='r')
axs[0,1].set_xlabel("frequência analógica em unidades de pi")
axs[0,1].set_ylabel("decibeis")
axs[0,1].axis([0,0.5,-30,5])

axs[1,1].set_title("Resposta do impulso")
axs[1,1].plot(t,ha)
axs[1,1].grid()
axs[1,1].set_xlabel("tempo (seg)")
axs[1,1].set_ylabel("ha(t)")

fig.tight_layout()

plt.show()