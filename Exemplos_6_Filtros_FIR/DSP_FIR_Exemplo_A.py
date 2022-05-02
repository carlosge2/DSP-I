# Filtro FIR exemplo A

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

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

# M = 5, janela retangular

wc = 0.5*np.pi
M=5
n=np.arange(M)

hd = ideal_lp(wc,M)
w_ret = signal.windows.boxcar(M)
h = hd * w_ret

[w, H] = signal.freqz(h,1)
fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('Resposta ao impulso ideal M=5')
axs[0,0].stem(n, hd)
axs[0,0].grid()
axs[0,0].set_xlabel("n")
axs[0,0].set_ylabel("hd[n]")

axs[1,0].set_title("Janela retangular")
axs[1,0].stem(n,w_ret)
axs[1,0].grid()
axs[1,0].set_xlabel("n")
axs[1,0].set_ylabel("w[n]")

axs[0,1].set_title("Resposta ao impulso real")
axs[0,1].stem(n,h)
axs[0,1].grid()
axs[0,1].set_xlabel("n")
axs[0,1].set_ylabel("h[n]")

axs[1,1].set_title("Resposta magnitude em dB")
axs[1,1].plot(w/np.pi,20*np.log10(np.abs(H)))
axs[1,1].grid()
axs[1,1].set_xlabel("frequência em unidades de pi")
axs[1,1].set_ylabel("dB")

fig.tight_layout()


# M = 6, janela retangular

wc = 0.5*np.pi
M=6
n=np.arange(M)

hd = ideal_lp(wc,M)
w_ret = signal.windows.boxcar(M)
h = hd * w_ret

[w, H] = signal.freqz(h,1)
fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('Resposta ao impulso ideal M=6')
axs[0,0].stem(n, hd)
axs[0,0].grid()
axs[0,0].set_xlabel("n")
axs[0,0].set_ylabel("hd[n]")

axs[1,0].set_title("Janela retangular")
axs[1,0].stem(n,w_ret)
axs[1,0].grid()
axs[1,0].set_xlabel("n")
axs[1,0].set_ylabel("w[n]")

axs[0,1].set_title("Resposta ao impulso real")
axs[0,1].stem(n,h)
axs[0,1].grid()
axs[0,1].set_xlabel("n")
axs[0,1].set_ylabel("h[n]")

axs[1,1].set_title("Resposta magnitude em dB")
axs[1,1].plot(w/np.pi,20*np.log10(np.abs(H)))
axs[1,1].grid()
axs[1,1].set_xlabel("frequência em unidades de pi")
axs[1,1].set_ylabel("dB")

fig.tight_layout()

# M = 7, janela retangular

wc = 0.5*np.pi
M=7
n=np.arange(M)

hd = ideal_lp(wc,M)
w_ret = signal.windows.boxcar(M)
h = hd * w_ret

[w, H] = signal.freqz(h,1)
fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0,0].set_title('Resposta ao impulso ideal M=7')
axs[0,0].stem(n, hd)
axs[0,0].grid()
axs[0,0].set_xlabel("n")
axs[0,0].set_ylabel("hd[n]")

axs[1,0].set_title("Janela retangular")
axs[1,0].stem(n,w_ret)
axs[1,0].grid()
axs[1,0].set_xlabel("n")
axs[1,0].set_ylabel("w[n]")

axs[0,1].set_title("Resposta ao impulso real")
axs[0,1].stem(n,h)
axs[0,1].grid()
axs[0,1].set_xlabel("n")
axs[0,1].set_ylabel("h[n]")

axs[1,1].set_title("Resposta magnitude em dB")
axs[1,1].plot(w/np.pi,20*np.log10(np.abs(H)))
axs[1,1].grid()
axs[1,1].set_xlabel("frequência em unidades de pi")
axs[1,1].set_ylabel("dB")

fig.tight_layout()


plt.show()
