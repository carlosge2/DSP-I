# Filtro FIR exemplo 7.8v2

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from fDSP_filtros import freqz_m
from plot_zplane import zplane


wp = 0.2*np.pi
ws = 0.3*np.pi
tr_width = ws - wp
M = np.ceil(6.6*np.pi/tr_width) + 1 # cálculo da ordem M
n=np.arange(M)
wc = (ws+wp)/2    # cálculo da freq. de corte
Rp = 0.25
As = 50

# usando função firwin
h = signal.firwin(int(M), wc/np.pi, window='hamming')

[db,mag,pha,grd,w] = freqz_m(h,1)

delta_w = np.pi/(len(w)-1)
Rp_calculado = -(np.min(db[0:int(wp/delta_w+1):]))       
As_calculado = -np.round(np.max(db[int(ws/delta_w):len(w)-1:]))

fig, axs = plt.subplots(nrows=2, ncols=1)


axs[0].set_title("Resposta ao impulso real")
axs[0].stem(n,h)
axs[0].grid()
axs[0].set_xlabel("n")
axs[0].set_ylabel("h[n]")

axs[1].set_title("Resposta magnitude em dB")
axs[1].plot(w/np.pi,db)
axs[1].grid()
axs[1].axhline(-Rp, color='r')
axs[1].axhline(-As, color='r')
axs[1].axvline(wp/np.pi, color='r')
axs[1].axvline(ws/np.pi, color='r')
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("dB")

fig.tight_layout()

fig, axs = plt.subplots(nrows=2, ncols=1)


axs[0].set_title("Fase")
axs[0].plot(w/np.pi,pha)
axs[0].grid()
axs[0].set_xlabel("frequência em unidades de pi")
axs[0].set_ylabel("rads")

axs[1].set_title("fase contínua")
axs[1].plot(w/np.pi,np.unwrap(pha))
axs[1].grid()
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("rads")


fig.tight_layout()

plt.figure()
plt.title("Diagrama de polos e zeros")
z,p,k = zplane(h,[1,0])


plt.show()