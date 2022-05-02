# Exemplo 8.27

import numpy as np
from scipy import signal
from fDSP_filtros import u_buttap,afd_butt,freqs_m,freqz_m,u_chb1ap,afd_chb1,imp_invr
import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
from plot_zplane import zplane

def zmapping(bZ,aZ,Nz,Dz):
    
    #  Frequency band Transformation from Z-domain to z-domain
    #  -------------------------------------------------------
    #  [bz,az] = zmapping(bZ,aZ,Nz,Dz)
    #  performs:
    #  b(z) b(Z)|
    #  ---- = ----| N(z)
    #  a(z) a(Z)|@Z = ----
    #  D(z)
    # 
    bNzord = (len(bZ)-1)*(len(Nz)-1)
    aDzord = (len(aZ)-1)*(len(Dz)-1)
    bzord = len(bZ)-1
    azord = len(aZ)-1
    bz = np.zeros(bNzord+1)
    for k in range(bzord+1):
        pln = np.array([1])
        for l in range(k):
            pln = np.convolve(pln,Nz)
        pld = np.array([1])
        for l in range(bzord-k):
            pld = np.convolve(pld,Dz)
        bz = bz+bZ[k]*np.convolve(pln,pld)

    az = np.zeros(aDzord+1)
    for k in range(azord+1):
        pln = np.array([1])
        for l in range(k):
            pln = np.convolve(pln,Nz)
        pld = np.array([1])
        for l in range(azord-k):
            pld = np.convolve(pld,Dz)
        az = az + aZ[k]*np.convolve(pln,pld)

    return bz,az

def cheb1hpf(wp,ws,Rp,As):
    #  IIR Highpass filter design using Chebyshev-1 prototype
    #  function [b,a] = cheb1hpf(wp,ws,Rp,As)
    #  b = Numerator polynomial of the highpass filter
    #  a = Denominator polynomial of the highpass filter
    #  wp = Passband frequency in radians
    #  ws = Stopband frequency in radians
    #  Rp = Passband ripple in dB
    #  As = Stopband attenuation in dB
    # 
    #  Determine the digital lowpass cutoff frequencies:
    wplp = 0.2*np.pi
    alpha = -(np.cos((wplp+wp)/2))/(np.cos((wplp-wp)/2))
    wslp = np.angle(-(np.exp(-1j*ws)+alpha)/(1+alpha*np.exp(-1j*ws)))
    
    # Compute Analog lowpass Prototype Specifications:
    T = 1; Fs = 1/T;
    OmegaP = (2/T)*np.tan(wplp/2)
    OmegaS = (2/T)*np.tan(wslp/2)
    # Design Analog Chebyshev Prototype Lowpass Filter:
    [cs,ds] = afd_chb1(OmegaP,OmegaS,Rp,As)
    # Perform Bilinear transformation to obtain digital lowpass
    [blp,alp] = signal.bilinear(cs,ds,Fs)
    # Transform digital lowpass into highpass filter
    Nz = -np.array([alpha,1])
    Dz = np.array([1,alpha])
    [b,a] = zmapping(blp,alp,Nz,Dz)
    return b,a

# Digital Highpass Filter Specifications:
wp = 0.6*np.pi    # digital Passband freq in rad
ws = 0.4586*np.pi # digital Stopband freq in rad
Rp = 1            # Passband ripple in dB
As = 15           # Stopband attenuation in dB

[b,a] = cheb1hpf(wp,ws,Rp,As)

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

pha[0]=0
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


              
              