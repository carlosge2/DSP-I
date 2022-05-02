import matplotlib.pyplot as plt
from fDSP import impseq,stepseq,sigadd,sigmult,sigshift,sigfold
import numpy as np

# exemplo 3.18

# Sinal analógico
Dt = 0.00005
t = np.arange(-100,101)*Dt
xa = np.exp(-1000*np.abs(t))

# Transformada de Fourier a tempo contínuo
Wmax = 2*np.pi*2000
K = 500
k = np.arange(K+1)
W = k*Wmax/K
Xa = [xa] @ np.exp(-1j*np.transpose([t])@[W]) * Dt
Xa = np.real(Xa)

W = np.concatenate((-np.flip([W]),[W]),axis=1) # Omega from -Wmax to Wmax
W=W[0]
Xa = np.concatenate((np.flip(Xa),Xa),1)    # Xa over -Wmax to Wmax interval
Xa=Xa[0]

fig, axs = plt.subplots(nrows=2, ncols=1)

axs[0].set_title("Sinal analógico")
axs[0].plot(t*1000,xa)
axs[0].grid()
axs[0].set_xlabel("t em msec.")
axs[0].set_ylabel("xa(t)")


axs[1].set_title("Transformada de Fourier a tempo contínuo")
axs[1].plot(W/(2*np.pi*1000),Xa*1000)
axs[1].grid()
axs[1].set_xlabel("frequência em KHz")
axs[1].set_ylabel("Xa(jW)*1000")

fig.tight_layout()

plt.show()