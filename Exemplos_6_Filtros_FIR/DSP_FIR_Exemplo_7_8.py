# Filtro FIR exemplo 7.8

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from fDSP_filtros import freqz_m

def ideal_lp(wc,M):
    # Ideal LowPass filter computation
    # --------------------------------
    # [hd] = ideal_lp(wc,M)
    # hd = ideal impulse response between 0 to M-1
    # wc = cutoff frequency in radians
    # M = length of the ideal filter
    alpha = (M-1)/2
    n = np.arange(M)
    m = n - alpha
    fc = wc/np.pi
    hd = fc*np.sinc(fc*m)
    return(hd)


wp = 0.2*np.pi
ws = 0.3*np.pi
tr_width = ws - wp
M = np.ceil(6.6*np.pi/tr_width) + 1 # cálculo da ordem M
n=np.arange(M)
wc = (ws+wp)/2    # cálculo da freq. de corte
Rp = 0.25
As = 50

hd = ideal_lp(wc,M)
w_ham = signal.windows.hamming(int(M))
h = hd * w_ham

[db,mag,pha,grd,w] = freqz_m(h,1)

delta_w = np.pi/(len(w)-1)
Rp_calculado = -(np.min(db[0:int(wp/delta_w+1):]))       
As_calculado = -np.round(np.max(db[int(ws/delta_w):len(w)-1:]))

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('Resposta ao impulso ideal')
axs[0,0].stem(n, hd)
axs[0,0].grid()
axs[0,0].set_xlabel("n")
axs[0,0].set_ylabel("hd[n]")

axs[1,0].set_title("Janela hamming")
axs[1,0].stem(n,w_ham)
axs[1,0].grid()
axs[1,0].set_xlabel("n")
axs[1,0].set_ylabel("w[n]")

axs[0,1].set_title("Resposta ao impulso real")
axs[0,1].stem(n,h)
axs[0,1].grid()
axs[0,1].set_xlabel("n")
axs[0,1].set_ylabel("h[n]")

axs[1,1].set_title("Resposta magnitude em dB")
axs[1,1].plot(w/np.pi,db)
axs[1,1].grid()
axs[1,1].axhline(-Rp, color='r')
axs[1,1].axhline(-As, color='r')
axs[1,1].axvline(wp/np.pi, color='r')
axs[1,1].axvline(ws/np.pi, color='r')
axs[1,1].set_xlabel("frequência em unidades de pi")
axs[1,1].set_ylabel("dB")

fig.tight_layout()

plt.show()