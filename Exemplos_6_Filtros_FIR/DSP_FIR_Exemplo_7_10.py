# Filtro FIR exemplo 7.10

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from fDSP_filtros import freqz_m
from plot_zplane import zplane

ws1 = 0.2*np.pi
wp1 = 0.35*np.pi
wp2 = 0.65*np.pi
ws2 = 0.8*np.pi
As = 60
Rp = 1

tr_width = min((wp1-ws1),(ws2-wp2))
M = np.ceil(11*np.pi/tr_width) + 2
n=np.arange(M)
wc1 = (ws1+wp1)/2
wc2 = (wp2+ws2)/2

# usando função firwin
h = signal.firwin(int(M), [wc1/np.pi,wc2/np.pi], pass_zero=False, window='blackman')

[db,mag,pha,grd,w] = freqz_m(h,1)

delta_w = np.pi/(len(w)-1)
Rp_calculado = -(np.min(db[int(wp1/delta_w+1):int(wp2/delta_w+1):]))       
As_calculado = -np.round(np.max(db[int(ws2/delta_w):len(w)-1:]))

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
axs[1].axvline(wp1/np.pi, color='r')
axs[1].axvline(ws1/np.pi, color='r')
axs[1].axvline(wp2/np.pi, color='r')
axs[1].axvline(ws2/np.pi, color='r')
axs[1].set_xlabel("frequência em unidades de pi")
axs[1].set_ylabel("dB")

fig.tight_layout()

plt.figure()
plt.title("Diagrama de polos e zeros")
z,p,k = zplane(h,[1,0])

plt.show()