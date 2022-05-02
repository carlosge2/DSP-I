# Exemplo 8.18

import numpy as np
from scipy import signal
from fDSP_filtros import u_buttap,afd_butt,freqs_m,freqz_m,u_chb1ap,afd_chb1,imp_invr
import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
from plot_zplane import zplane

# Digital Filter Specifications
wp = 0.2*np.pi   # digital Passband freq in rad/s
ws = 0.3*np.pi   # digital Stopband freq in rad/s
Rp = 1           # Passband ripple in dB
As = 15          # Stopband attenuation in dB

# Analog Prototype Specifications: Inverse mapping for frequencies
T = 1             # Set T=1
Fs = 1/T
#OmegaP = wp / T  # Prototype Passband freq
#OmegaS = ws / T  # Prototype Stopband freq
OmegaP = (2/T)*np.tan(wp/2)      # Prewarp Prototype Passband freq
OmegaS = (2/T)*np.tan(ws/2)      # Prewarp Prototype Stopband freq

ep = np.sqrt(10**(Rp/10)-1)     # Passband Ripple parameter
Ripple = np.sqrt(1/(1+ep*ep))   # Passband Ripple
Attn = 1/(10**(As/20))          # Stopband Attenuation

# Analog Chebyshev-I Prototype Filter Calculation
[cs,ds] = afd_chb1(OmegaP,OmegaS,Rp,As)

# Bilinear transformation
[b,a] = signal.bilinear(cs,ds,Fs)

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

# Calculation of Impulse response
t=np.arange(0,30,0.1)
t,ha = signal.impulse((cs,ds),T=t)

# Impulse response of the digital filter
n = np.arange(0,30/T,1)
delta,n = impseq(0,0,int(30/T))
hn = signal.lfilter(b,a,delta)

# Magnitude Response of the digital filter
[db,magd,pha,grd,wd] = freqz_m(b,a)

# magnitude response of the analog filter
[db,mags,pha,ws] = freqs_m(cs,ds,2*np.pi/T)


fig, axs = plt.subplots(nrows=2, ncols=1)
axs[0].set_title("Respostas ao impulso")
axs[0].plot(t,ha,color='r')
axs[0].stem(n*T,hn)
axs[0].grid()
axs[0].set_xlabel("tempo (seg)")
axs[0].set_ylabel('amplitude')

axs[1].set_title("Respostas de magnitude")
axs[1].plot(ws/(2*np.pi),mags/T,wd/(2*np.pi)/T,magd)
axs[1].grid()
axs[1].set_xlabel("frequência em Hz")
axs[1].set_ylabel('magnitude')

fig.tight_layout()

plt.figure()
plt.title("Diagrama de polos e zeros")
z,p,k = zplane(b,a)

plt.show()
